from pathlib import Path

import yaml
import sys

from utils.filesystem import path_to_data_directory

ModRootDirectory: Path = path_to_data_directory("TheCrew")
LanguageDirectory: Path = ModRootDirectory / "Language"
PediaDirectory: Path = ModRootDirectory / "Resources/Pedia"
RulesetDirectory: Path = ModRootDirectory / "Ruleset"

LanguageFile: Path = LanguageDirectory / "en-US.yml"
RulesFile: Path = RulesetDirectory / "TheCrew_Resources.rul"


def add_ufopedia_entry(
    title: str,
    content: str,
    resource_file_path: Path,
) -> None:
    # Load en-US.yml
    with open(LanguageFile.as_posix(), "r") as file:
        language_data = yaml.safe_load(file)

    # Load mod.rul
    with open(RulesFile.as_posix(), "r") as file:
        mod_rul_data = yaml.safe_load(file)

    # Generate IDs
    base_id = title.replace(" ", "_").upper()
    text_id = f"STR_{base_id}_UFOPEDIA"
    image_id = base_id

    # Update en-US.yml
    language_data["en-US"][f"STR_{base_id}"] = title
    language_data["en-US"][text_id] = content

    # Update mod.rul
    mod_rul_data["ufopaedia"].append(
        {
            "id": f"STR_{base_id}",
            "type_id": 7,
            "section": "STR_UFO_COMPONENTS",
            "text": text_id,
            "image_id": image_id,
            "text_width": 140,
        }
    )
    mod_rul_data["extraSprites"].append({"typeSingle": image_id, "fileSingle": resource_file_path.as_posix()})

    with open(LanguageFile.as_posix(), "w") as file:
        yaml.dump(language_data, file)

    with open(RulesFile.as_posix(), "w") as file:
        yaml.dump(mod_rul_data, file)


# Read arguments from command line
if len(sys.argv) != 4:
    print("Usage: python update_yaml.py <title> <content> <resource_file_path>")
else:
    # Ensure the output path is a Path object
    output_path = Path(sys.argv[3])
    # Create directories if they do not exist
    output_path.parent.mkdir(parents=True, exist_ok=True)
    add_ufopedia_entry(sys.argv[1], sys.argv[2], output_path)
