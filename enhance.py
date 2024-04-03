from PIL import Image, ImageEnhance

image = Image.open("cat.jpg")

# create the enhancer
enhancer = ImageEnhance.Color(image)
contract_enhancer = ImageEnhance.Contrast(image)
brightness_enhancer = ImageEnhance.Brightness(image)
sharpness_enhancer = ImageEnhance.Sharpness(image)
# apply the enhancer
enhanced_image = enhancer.enhance(2.5)


enhanced_image.show()