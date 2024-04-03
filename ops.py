from PIL import Image, ImageOps

image = Image.open('dog.jpg')

# invert, add a border, mirror the image
image_invert = ImageOps.invert(image)
image_border = ImageOps.expand(image_invert, border=20, fill='black')
image_mirror = ImageOps.mirror(image_border)
image_scaled = ImageOps.scale(image_mirror, 0.5)

# color changes
image_gray = ImageOps.grayscale(image_scaled)

image_gray.show()