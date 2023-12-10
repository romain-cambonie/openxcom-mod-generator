import base64
from pathlib import Path

from openai import OpenAI
from openai.types.chat import ChatCompletion


# Function to encode the image to base64
def encode_image(path: Path) -> str:
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# Encoding the image


def describe_image(client: OpenAI, image_path: Path) -> str:
    """
    Function to get a description of an image using OpenAI's GPT-4 Vision model.

    Parameters:
    client (OpenAI): The OpenAI client object.
    image_url (str): URL of the image to be described.

    Returns:
    dict: The response from the OpenAI API.
    """
    base64_image = encode_image(image_path)

    response: ChatCompletion = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe in details the character in this pixel-art image, respond in JSON."},
                    {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{base64_image}", "detail": "low"}},
                ],
            }
        ],
        max_tokens=800,
    )

    choice = response.choices[0]
    return str(choice.message.content)
