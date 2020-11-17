from PIL import Image

image = Image.open('joe-cleary-CfANlkglvUc-unsplash.jpg')
new_image = image.resize((400, 400))
new_image.save('image_400.jpg')

print(image.size) # Output: (1200, 776)
print(new_image.size) # Output: (400, 400)