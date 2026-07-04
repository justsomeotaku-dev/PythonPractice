from PIL import Image, ImageEnhance

img = Image.open('Yahu.jpg')

enhancer = ImageEnhance.Contrast(img)
img_contrast = enhancer.enhance(2) # 400%

img_contrast.show()