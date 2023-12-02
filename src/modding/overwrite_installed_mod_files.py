from pathlib import Path

from utils.filesystem import copy_recursive


def overwrite_installed_mod_files(mod_development_directory: Path, installation_directory_to_replace: Path) -> None:
    copy_recursive(mod_development_directory, installation_directory_to_replace)
