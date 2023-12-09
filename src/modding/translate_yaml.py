import yaml
from typing import Any, Dict, List, Union


def translate() -> None:
    # Load the payload and language files
    with open("/home/yandros/Games/OpenXcom/share/openxcom/user/mods/TheCrew/GameData/payload.yaml", "r") as file:
        payload: Dict[str, Any] = yaml.safe_load(file)

    with open("/home/yandros/Games/OpenXcom/share/openxcom/user/mods/Piratez/Language/en-US.yml", "r") as file:
        language_data: Dict[str, Dict[str, str]] = yaml.safe_load(file)

    language_translations: Dict[str, str] = language_data.get("en-US", {})

    root_keys_to_keep: List[str] = [
        "armor",
        "armorDescription",
        "equipmentLayout",
        "gender",
        "kills",
        "look",
        "lookVariant",
        "missions",
        "name",
        "nationality",
        "rank",
        "type",
    ]

    # Process for item descriptions
    processed_payload: Dict[str, Any] = {k: process_items(v, k) for k, v in payload.items() if k in root_keys_to_keep}

    # Special processing for 'armor' key
    if "armor" in processed_payload:
        armor_description: str = processed_payload["armor"] + "_UFOPEDIA"
        processed_payload["armorDescription"] = armor_description

    # Translate the payload
    translated_payload: Dict[str, Any] = {k: translate_payload(v, language_translations) for k, v in processed_payload.items()}

    # Write the translated payload to a new file
    with open("/home/yandros/Games/OpenXcom/share/openxcom/user/mods/TheCrew/GameData/payload-translated.yml", "w") as file:
        yaml.dump(translated_payload, file)


def process_items(data: Any, root_key: str) -> Any:
    if root_key == "equipmentLayout" and isinstance(data, list):
        return [process_list_item(item) for item in data]
    return data


def process_list_item(item: Union[Dict[str, str], str]) -> Union[Dict[str, str], str]:
    if isinstance(item, dict) and "itemType" in item:
        item["description"] = item["itemType"] + "_UFOPEDIA"
    return item


def translate_payload(data: Any, translations: Dict[str, str]) -> Any:
    if isinstance(data, dict):
        return {key: translate_payload(value, translations) for key, value in data.items()}
    elif isinstance(data, list):
        return [translate_payload(item, translations) for item in data]
    elif isinstance(data, str) and data.startswith("STR_"):
        return translations.get(data, data)
    else:
        return data
