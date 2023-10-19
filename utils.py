import os
from PIL import Image


def change_aspect_ratio(image_path):
    # Open the image
    image = Image.open(image_path)

    # Calculate the new height to achieve a 4:5 aspect ratio
    new_width = int(image.width * 4 / 5)
    new_height = int(image.height * 5 / 4)

    # Resize the image to the new aspect ratio
    image = image.resize((new_width, new_height))

    # Save the modified image
    image.save(image_path)

    return image


def env(name):
    return os.getenv(name)
