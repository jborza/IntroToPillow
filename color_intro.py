from PIL import Image

image = Image.open("checkerboard.png")

px = image.getpixel((0, 0))
print(px)

# grayscale image
grayscale_image = image.getchannel("R")

# change the pixel color
# image.putpixel((0, 0), (255, 0, 0))

# change all of the black pixels to red
for x in range(image.width):
    for y in range(image.height):
        if image.getpixel((x, y))[0] == 0:
            image.putpixel((x, y), (255, 0, 0))

image.show()