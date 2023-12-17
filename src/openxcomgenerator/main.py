#!/usr/bin/env python3
# from pathlib import Path
from pathlib import Path
from typing import Dict
import sys
import json
import openai
from casefy import kebabcase  # type: ignore[attr-defined]

from chat.ask_for_dalle_character_prompt import ask_for_dalle_character_prompt
from chat.ask_for_origin_story import ask_for_origin_story
from chat.ask_for_visual_proposition import ask_for_concept_art
from chat.image_description import describe_image
from dalle.call_dalle_and_save_image import call_dalle_and_save_image
from image.crop import crop_image_to_square
from image.paint_black_rectangle import paint_black_rectangle
from modding.translate_yaml import translate
from utils.dotenv import EnvironmentVariables, get_environment_variables_from_dotenv


# from conversion.convert_image_to_resource import convert_to_ufopedia_ready_image
# from gpt.ask_for_dalle_prompt import ask_for_dalle_prompt
# from dalle.image_generation import call_dalle_and_save_image
# from gpt.ask_for_origin_story import ask_for_origin_story
# from modding.add_ufopedia_entry import add_ufopedia_entry
# from modding.overwrite_installed_mod_files import overwrite_installed_mod_files
# from utils.dotenv import get_environment_variables_from_dotenv, EnvironmentVariables
# from utils.filesystem import path_to_data_directory

# This script can be called though the game executable
# The only registered command for now is 'generateBackstory'


# Write the given string content to a given file path
def save(content: str, path: Path) -> None:
    with open(path.as_posix(), "w") as file:
        file.write(content)


def main(json_payload_string: str) -> None:
    # Parse the JSON string into a Python dictionary
    args: Dict[str, str] = json.loads(json_payload_string)

    # Extract the command and paths
    print("command", args["command"])
    print("payloadPath", args["payload"])
    print("screenshotPath", args["screenshot"])

    env: EnvironmentVariables = get_environment_variables_from_dotenv()

    # Translate game payload
    # As of now payload contains the path to the payload.yml generated from the character Yaml:Node in the game.
    payload_file: Path = Path(args["payload"])
    language_filename: str = env["LANGUAGE_LOCALE"] + ".yml"
    language_file: Path = Path(env["LANGUAGE_DIRECTORY"]) / language_filename
    payload_localized_output_path: Path = Path(env["WORKING_DIRECTORY"]) / "payload-translated.yml"
    locale: str = env["LANGUAGE_LOCALE"]
    #
    # Localize the yaml payload using the game (mod) files to have the full text
    # description of what the character in wearing and equipped with
    character_name: str = translate(
        payload_path=payload_file,
        language_path=language_file,
        payload_localized_output_path=payload_localized_output_path,
        locale=locale,
    )

    character_identifier = kebabcase(character_name)

    with open(payload_localized_output_path, "r") as file:
        character_game_description = file.read()

    print(f"Character equipment translation done. Saved to: {payload_localized_output_path.as_posix()}")

    # Describe screenshot
    game_screenshot: Path = Path(args["screenshot"])
    cropped_image_gpt4_vision: Path = Path(env["WORKING_DIRECTORY"]) / "image-cropped.png"

    # Crop image to 512x512 square
    # For my resolution of 2560x1440 the top-left corner of the 512x512 crop-box is, in a 0..1 coordinate format.
    top_left_x = 0.275
    top_left_y = 0.288
    crop_image_to_square(
        image_path=game_screenshot,
        output_path=cropped_image_gpt4_vision,
        crop_top_left_x_percent=top_left_x,
        crop_top_left_y_percent=top_left_y,
    )

    # add 132x512 black rectangle to hide left inventory starting at 0
    paint_black_rectangle(
        image_path=cropped_image_gpt4_vision, output_path=cropped_image_gpt4_vision, start_x=0, start_y=0, width=132, height=512
    )
    # add 128x512 black rectangle to hide right inventory starting at 384
    paint_black_rectangle(
        image_path=cropped_image_gpt4_vision,
        output_path=cropped_image_gpt4_vision,
        start_x=384,
        start_y=0,
        width=128,
        height=512,
    )

    # Ask for image description
    open_ai_client = openai.OpenAI(
        api_key=env["OPEN_AI_API_KEY"],
    )

    character_image_description = describe_image(client=open_ai_client, image_path=cropped_image_gpt4_vision)

    output_vision: Path = Path(env["WORKING_DIRECTORY"]) / f"{character_identifier}-gpt4-vision-description.txt"
    save(character_image_description, output_vision)
    print(f"Character equipment description done, saved to: {output_vision.as_posix()}")

    # Generate Origin Story
    story: str = ask_for_origin_story(
        client=open_ai_client,
        character_name=character_name,
        equipment_description=character_game_description,
        appearance_description=character_image_description,
    )

    output_story: Path = Path(env["WORKING_DIRECTORY"]) / f"{character_identifier}-gpt4-vision-origin-story.txt"
    save(story, output_story)
    print(f"Character origin story generated, saved to: {output_story.as_posix()}")

    # Generate concept art
    art_style: str = (
        "digital concept art style, resembling modern video game illustrations. "
        "The character should be depicted in ultra-high definition with sharp details, vibrant colors, and clean lines."
        "Aim for a sleek digital look with smooth textures, and dynamic lighting effects"
    )
    concept_art_description: str = ask_for_concept_art(
        client=open_ai_client,
        character_story=story,
        art_style_description=art_style,
    )

    output_concept_art: Path = Path(env["WORKING_DIRECTORY"]) / f"{character_identifier}-gpt4-concept-art.txt"
    save(concept_art_description, output_concept_art)
    print(f"Description of concept art generated, saved to: {output_concept_art.as_posix()}")

    # Refine to Prompt
    prompt: str = ask_for_dalle_character_prompt(
        client=open_ai_client,
        concept_art_description=concept_art_description,
    )

    output_dalle_prompt: Path = Path(env["WORKING_DIRECTORY"]) / f"{character_identifier}-gpt4-dalle-prompt.txt"
    save(prompt, output_dalle_prompt)
    print(f"Character dalle prompt generated, saved to: {output_dalle_prompt.as_posix()}")

    # Generate Image
    output_path: Path = Path(env["WORKING_DIRECTORY"]) / f"{character_identifier}.png"
    call_dalle_and_save_image(prompt=prompt, client=open_ai_client, output_file_path=output_path)

    print(f"Character image generated, saved to: {output_path.as_posix()}")
    # 3: prompt engineering following lucille and retro system prompt
    # 3-2: ask for embedding and seed for persistence


#
# character_name: str = "Awesome Rhino"
#
# prompt: str = ask_for_dalle_prompt()
# character_story: str = ask_for_origin_story()
#
# rawPath: Path = path_to_data_directory("raws") / "raw.png"
#
# pathAsUfopediaResource: Path = path_to_data_directory("TheCrew") / "Resources" / "Pedia"
# mod_dev_directory: Path = path_to_data_directory("TheCrew")
# mod_game_directory_to_overwrite: Path = Path("/home/yandros/Games/OpenXcom/share/openxcom/user/mods")
# call_dalle_and_save_image(prompt=prompt, api_key=env["OPEN_AI_API_KEY"], output_file_path=rawPath)
# convert_to_ufopedia_ready_image(input_file_path=rawPath, output_file_path=pathAsUfopediaResource)
# add_ufopedia_entry(title=character_name, content=character_story, resource_file_path=pathAsUfopediaResource)
# overwrite_installed_mod_files(mod_dev_directory, mod_game_directory_to_overwrite)


if __name__ == "__main__":
    main(sys.argv[1])
