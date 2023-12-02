import shutil
from pathlib import Path


def find_src_directory() -> Path:
    current_dir = Path(__file__).resolve().parent

    while current_dir.name != "src" and current_dir.parent != current_dir:
        current_dir = current_dir.parent

    if current_dir.name != "src":
        raise FileNotFoundError("Parent directory 'src' not found.")

    return current_dir


def find_data_directory() -> Path:
    src_dir = find_src_directory()
    data_dir = src_dir.parent / "data"

    # Check if 'data' directory exists
    if not data_dir.exists() or not data_dir.is_dir():
        raise FileNotFoundError("Data directory not found adjacent to 'src' directory.")

    return data_dir


def path_to_data_file(filename: str) -> Path:
    data_dir = find_data_directory()
    file_path = data_dir / filename

    # Check if the file exists
    if not file_path.exists():
        raise FileNotFoundError(f"The file '{filename}' was not found in the data directory.")

    return file_path


def path_to_data_directory(directory: str) -> Path:
    data_dir = find_data_directory()
    directory_path = data_dir / directory

    if not directory_path.is_dir():
        directory_path.mkdir(parents=True, exist_ok=True)

    return directory_path


def get_first_matching_data_file(directory: str, pattern: str) -> Path:
    return next(path_to_data_directory(directory).glob(f"{pattern}.*"))


def copy_recursive(input_directory: Path, output_directory: Path) -> None:
    # Ensure inputDirectory is a directory
    if not input_directory.is_dir():
        raise ValueError(f"The input path {input_directory} is not a directory.")

    # If outputDirectory exists, delete it
    if output_directory.exists():
        shutil.rmtree(output_directory)

    # Copy the entire directory tree from inputDirectory to outputDirectory
    shutil.copytree(input_directory, output_directory)
