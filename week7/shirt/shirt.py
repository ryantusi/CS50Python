# Import Libraries
import os
import sys
import PIL
from PIL import Image

# Checking command line arguments validity
if len(sys.argv) == 3:
    # storing the names of input and output files
    inp = sys.argv[1].lower()
    out = sys.argv[2].lower()

    # splitting file name and extension
    in_file, in_ext = os.path.splitext(inp)
    out_file, out_ext = os.path.splitext(out)

    # list of acceptable extension
    ext = [".jpg", ".jpeg", ".png"]

    # Checking if both extensions are same
    if in_ext != out_ext:
        sys.exit("Not same extension")

    # Checking if extensions are image format
    if (in_ext not in ext) or (out_ext not in ext):
        sys.exit("Only extensions supported: .jpg | .jpeg | .png")

    # Opening shirt image
    try:
        shirt = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt file does not exist")
    except PIL.UnidentifiedImageError:
        sys.exit("Shirt file not in image format")

    # Opening the image
    try:
        img = Image.open(inp)
    except FileNotFoundError:
        sys.exit("No such file exists")
    except PIL.UnidentifiedImageError:
        sys.exit("Not in image format")

    # Resizing the image to shirt image size
    image_resized = PIL.ImageOps.fit(img, shirt.size)

    # Masking the shirt image to the resized image file
    image_resized.paste(shirt, shirt)

    # Saving the result in the output file name and extension
    image_resized.save(
        out
    )

# Invalid command line arguments 
else:
    sys.exit("Usage: python shirt.py input output")
