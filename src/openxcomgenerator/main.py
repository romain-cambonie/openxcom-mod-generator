from pathlib import Path

from conversion.convert_image_to_resource import convert_to_ufopedia_ready_image
from gpt.ask_for_dalle_prompt import ask_for_dalle_prompt
from dalle.image_generation import call_dalle_and_save_image
from gpt.ask_for_origin_story import ask_for_origin_story
from modding.add_ufopedia_entry import add_ufopedia_entry
from modding.overwrite_installed_mod_files import overwrite_installed_mod_files
from utils.dotenv import get_environment_variables_from_dotenv, EnvironmentVariables
from utils.filesystem import path_to_data_directory


def main() -> None:
    print("Hello, this is an example pipeline !")

    env: EnvironmentVariables = get_environment_variables_from_dotenv()

    character_name: str = "Awesome Rhino"

    prompt: str = ask_for_dalle_prompt()
    character_story: str = ask_for_origin_story()

    rawPath: Path = path_to_data_directory("raws") / "raw.png"

    pathAsUfopediaResource: Path = path_to_data_directory("TheCrew") / "Resources" / "Pedia"

    mod_dev_directory: Path = path_to_data_directory("TheCrew")
    mod_game_directory_to_overwrite: Path = Path("/home/yandros/Games/OpenXcom/share/openxcom/user/mods")

    call_dalle_and_save_image(prompt=prompt, api_key=env["OPEN_AI_API_KEY"], output_file_path=rawPath)

    convert_to_ufopedia_ready_image(input_file_path=rawPath, output_file_path=pathAsUfopediaResource)

    add_ufopedia_entry(title=character_name, content=character_story, resource_file_path=pathAsUfopediaResource)
    overwrite_installed_mod_files(mod_dev_directory, mod_game_directory_to_overwrite)
    print("Entry added, reload the mod in game")


if __name__ == "__main__":
    main()
