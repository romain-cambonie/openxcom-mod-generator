from pathlib import Path
from PIL import Image


def paint_black_rectangle(image_path: Path, output_path: Path, start_x: int, start_y: int, width: int, height: int) -> Path:
    """
    Paints a black rectangle over a 512x512 image at the specified location and of the specified size.

    Parameters:
    image_path (str): The path to the original image.
    output_path (str): The path to save the modified image.
    start_x (int): The x-coordinate of the top-left corner of the rectangle.
    start_y (int): The y-coordinate of the top-left corner of the rectangle.
    width (int): The width of the rectangle.
    height (int): The height of the rectangle.
    """
    # Open the original image
    with Image.open(image_path) as img:
        # Create a black rectangle
        black_rect = Image.new("RGB", (width, height), (0, 0, 0))
        # Paste the black rectangle onto the original image
        img.paste(black_rect, (start_x, start_y))

        # Save the edited image
        img.save(output_path)

    return output_path
