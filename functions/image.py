from PIL import Image

image = Image.open('joe-cleary-CfANlkglvUc-unsplash.jpg')
image.show()

# The file format of the source file.
print(image.format) # Output: JPEG

# The pixel format used by the image. Typical values are “1”, “L”, “RGB”, or “CMYK.”
print(image.mode) # Output: RGB

# Image size, in pixels. The size is given as a 2-tuple (width, height).
print(image.size) # Output: (1200, 776)

# Colour palette table, if any.
print(image.palette) # Output: None

image = Image.open('joe-cleary-CfANlkglvUc-unsplash.jpg')


image.save('new_image.png') #сохранение в новом формате, после изменений
#image.save('new_image.png', 'PNG') #сохранение в новом формате, после изменений для НЕСТАНДАРТНЫХ расширений, вы всегда должны указывать формат таким образом

image = Image.open('joe-cleary-CfANlkglvUc-unsplash.jpg')
new_image = image.resize((400, 400))
new_image.save('image_400.jpg')

print(image.size) # Output: (1200, 776)
print(new_image.size) # Output: (400, 400)