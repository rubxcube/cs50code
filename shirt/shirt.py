# Program that overlays shirt on image

import sys
from os.path import splitext
from PIL import Image, ImageOps


def shirt_overlay():

    # Checking command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    pic1 = sys.argv[1].lower()
    pic2 = sys.argv[2].lower()

    root1, ext1 = splitext(pic1)
    root2, ext2 = splitext(pic2)

    if len(sys.argv) == 2:
        if ext1 not in (".jpg", ".jpeg", ".png") and ext2 not in (
            ".jpg",
            ".jpeg",
            ".png",
        ):
            sys.exit("Invalid input")

    if ext1 != ext2:
        sys.exit("Input and output have different extensions")

    try:
        # Generating images to format
        before = Image.open(pic1)
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Input does not exist")
    else:
        size = shirt.size
        before_resized = ImageOps.fit(before, size)
        before_resized.paste(shirt, shirt)
        before_resized.save(pic2)


if __name__ == "__main__":
    shirt_overlay()
