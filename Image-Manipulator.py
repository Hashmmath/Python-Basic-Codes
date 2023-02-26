'''In this example, we first open an image file using the 
Image class from the Pillow library. Then, we resize the image, 
rotate it, convert it to grayscale, and apply a sharpen filter 
to it. Finally, we crop the image and save the modified image 
to a new file. You can modify this code to perform other image 
manipulation tasks such as changing the brightness or contrast
, adding text or shapes, and more.'''


from PIL import Image, ImageFilter

# Open an image file
image = Image.open('example.jpg')

# Resize the image
image = image.resize((500, 500))

# Rotate the image
image = image.rotate(90)

# Convert the image to grayscale
image = image.convert('L')

# Apply a filter to the image
image = image.filter(ImageFilter.SHARPEN)

# Crop the image
box = (100, 100, 400, 400)
image = image.crop(box)

# Save the modified image
image.save('modified.jpg')
