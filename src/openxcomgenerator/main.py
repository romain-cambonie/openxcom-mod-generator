#!/usr/bin/env python3
# from pathlib import Path
from typing import Any
import sys

# from conversion.convert_image_to_resource import convert_to_ufopedia_ready_image
# from gpt.ask_for_dalle_prompt import ask_for_dalle_prompt
# from dalle.image_generation import call_dalle_and_save_image
# from gpt.ask_for_origin_story import ask_for_origin_story
# from modding.add_ufopedia_entry import add_ufopedia_entry
# from modding.overwrite_installed_mod_files import overwrite_installed_mod_files
# from utils.dotenv import get_environment_variables_from_dotenv, EnvironmentVariables
# from utils.filesystem import path_to_data_directory


def main(command: str, payload: Any) -> None:
    # image = Image.open(image_path)
    # Do something with the image and data
    # print("Command received:", command)
    # print("Data received:", payload)

    # Write the serialized data to a text file
    with open("/home/yandros/Games/OpenXcom/share/openxcom/user/mods/TheCrew/debug_output.txt", "w") as file:
        file.write(command + " " + payload)

    # env: EnvironmentVariables = get_environment_variables_from_dotenv()


#
# character_name: str = "Awesome Rhino"
#
# prompt: str = ask_for_dalle_prompt()
# character_story: str = ask_for_origin_story()
#
# rawPath: Path = path_to_data_directory("raws") / "raw.png"
#
# pathAsUfopediaResource: Path = path_to_data_directory("TheCrew") / "Resources" / "Pedia"
#
# mod_dev_directory: Path = path_to_data_directory("TheCrew")
# mod_game_directory_to_overwrite: Path = Path("/home/yandros/Games/OpenXcom/share/openxcom/user/mods")
#
# call_dalle_and_save_image(prompt=prompt, api_key=env["OPEN_AI_API_KEY"], output_file_path=rawPath)
#
# convert_to_ufopedia_ready_image(input_file_path=rawPath, output_file_path=pathAsUfopediaResource)
#
# add_ufopedia_entry(title=character_name, content=character_story, resource_file_path=pathAsUfopediaResource)
# overwrite_installed_mod_files(mod_dev_directory, mod_game_directory_to_overwrite)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
