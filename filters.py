from PIL import Image, ImageFilter

image = Image.open('cat.jpg')

# apply a basic filter
image_blur = image.filter(ImageFilter.BLUR)
image_contour = image.filter(ImageFilter.CONTOUR)
image_emboss = image.filter(ImageFilter.EMBOSS)
image_edge = image.filter(ImageFilter.FIND_EDGES)

# apply an advanced filter
image_boxblur = image.filter(ImageFilter.BoxBlur(20))

image_boxblur.show()
