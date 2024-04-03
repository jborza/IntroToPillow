import PIL
from PIL import Image

# Open an image file
image = Image.open("..\\Assets-IntroPillow\\cat.jpg")

print(image.size)
print(image.format)

# flip the image
image = image.transpose(PIL.Image.FLIP_LEFT_RIGHT)

# Show the image
image.show()