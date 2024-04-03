from PIL import Image

# Open an image file
image = Image.open("cat.jpg")

# manipulate the image
image_rotate = image.rotate(30, expand=False)

# crop
image_crop = image.crop((800, 600, 1600, 1600))

# resize
image_resize = image.resize((1000, 600))

image_combined = image.transpose(Image.FLIP_LEFT_RIGHT).rotate(30, expand=False).crop((800, 600, 1600, 1600)).resize((1000, 600))   


image_combined.show()