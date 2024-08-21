from PIL import Image, ImageDraw, ImageFont

import math

# open image ...jpg, png, gif,..
img = Image.open("IMG_file.jpg") # image found from this project dir.
# img = Image.open("/home/<user>/Pictures/Photo_path.jpg")  # image path to project
# check the size of an image
width, height = img.size
# print(width, height)

pix = img.load()

# loop
for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        # print(r)
        h = int(r / 3 + g / 3 + b / 3)
        pix[j, i] = (h, h, h)
# save the image(black&white)...(png, jpg, ..) into the project dir.
img.save("Output_gray.jpg")
# img.save("IMG_BW.png")
print("SAVED\n" + "\nOpen the file, Copy commandline: eog Output_gary.jpg")
