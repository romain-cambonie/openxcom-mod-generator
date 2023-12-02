import sys
from pathlib import Path

import requests
import json


def call_dalle_and_save_image(prompt: str, api_key: str, output_file_path: Path) -> Path:
    url = "https://api.openai.com/v1/images/generations"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    payload = {"model": "dall-e-3", "prompt": prompt, "n": 1, "size": "1024x1024", "quality": "hd", "response_format": "url"}

    # Make the API call
    response = requests.post(url, headers=headers, json=payload)

    # Check for successful response
    if response.status_code == 200:
        # Load the response as a JSON object
        response_data = json.loads(response.text)

        # Extract the image URL
        image_url = response_data["data"][0]["url"]

        # Download the image from the URL
        image_response = requests.get(image_url)
        if image_response.status_code == 200:
            # Write the image data to a file
            with open(output_file_path.as_posix(), "wb") as file:
                file.write(image_response.content)
            print(f"Image downloaded and saved to {output_file_path.as_posix()}")
        else:
            print(f"Error downloading image: {image_response.status_code}")

    else:
        print(f"Error: {response.status_code}")
        print(response.text)

    return output_file_path


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: script.py <prompt> <api_key> <output_file_path>")
        sys.exit(1)

    prompt = sys.argv[1]
    api_key = sys.argv[2]
    output_file_path = sys.argv[3]

    # Ensure the output path is a Path object
    output_path = Path(output_file_path)

    # Create directories if they do not exist
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Call the function with command line arguments
    call_dalle_and_save_image(prompt, api_key, output_path)
