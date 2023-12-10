from pathlib import Path

from PIL import Image


def crop_image_to_square(
    image_path: Path, output_path: Path, crop_top_left_x_percent: float, crop_top_left_y_percent: float, crop_size: int = 512
) -> Path:
    with Image.open(image_path) as img:
        x_coordinate = int(img.width * crop_top_left_x_percent)
        y_coordinate = int(img.height * crop_top_left_y_percent)
        crop_box = (x_coordinate, y_coordinate, x_coordinate + crop_size, y_coordinate + crop_size)
        cropped_img = img.crop(crop_box)
        cropped_img.save(output_path)

        return output_path
