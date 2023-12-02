import subprocess
from pathlib import Path
from utils.filesystem import find_src_directory


def convert_to_ufopedia_ready_image(input_file_path: Path, output_file_path: Path) -> None:
    modulePath: Path = find_src_directory() / "conversion"
    scriptPath: Path = modulePath / "process_image_to_resource.sh"
    try:
        # The path to the script must be correct. Adjust if necessary.
        result = subprocess.run(
            [modulePath.as_posix() / scriptPath, input_file_path, "XCOM-Ufopaedia", output_file_path],
            check=True,
            text=True,
            capture_output=True,
        )
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr}")
