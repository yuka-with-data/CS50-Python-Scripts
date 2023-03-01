# Problem Set: https://cs50.harvard.edu/python/2022/psets/6/shirt/
""" 
Implement a program that expects exactly 2 command-line arguments (input and ouput)
The program should then overlay shirt.png on the input file,
after resizing and cropping the input to be the same size.
Save the result as its output. 

The program should exit via sys.exit:
if the user doesn't specify exactly 2 command-line arguments,
if the user input's and output's names do not end in .jpg, .jpeg, or .png, case-insensitively,
if the input's name does not have the same extension as the output's name, or
if the specifies input does not exist.

 """
# import libraries
import sys
from os.path import splitext
from PIL import Image, ImageOps

# shirt.py (before.png) (after file with a shirt image on)
def command_line_check():
    # if few CLA
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # if more CLA
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # extract ext lowercased
    ext1 = splitext(sys.argv[1].lower())[1]
    ext2 = splitext(sys.argv[2].lower())[1]
    if not ext1 == ext2:
        sys.exit("Input and Output have different extensions")
    # if ext is not png, jpeg, jpg
    extension = (".png", ".jpeg", ".jpg")
    if ext1 not in extension:
        sys.exit("Invalid file")

def image_edit():
    try:
        with (
            # open input file
            Image.open(sys.argv[1], mode='r') as input_image,
            # open shirt file
            Image.open("shirt.png", mode='r') as shirt
        ):
            # get a size of shirt image
            size = shirt.size
                # fit the input image based on the shirt image size
            resized_image = ImageOps.fit(input_image, size)
                # paste shirt.png on top of input image
            resized_image.paste(shirt, (0,0), shirt)
            resized_image.save(sys.argv[2])
            print(f"Image was successfully saved into {sys.argv[2]}")
    except (ValueError, OSError, EOFError, AttributeError):
        sys.exit("Errow while saving the image")
    # return sys.argv[2]

def main():
    command_line_check()
    image_edit()

if __name__ == "__main__":
    main()