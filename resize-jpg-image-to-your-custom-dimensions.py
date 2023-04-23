from PIL import Image
import glob
import os

# FInding all JPG images in the folder  
lst_imgs = [i for i in glob.glob("*.jpg")]
print(lst_imgs)

# Your custom width and height
height = 1024
width = 1024

# Converting images
for i in lst_imgs:
	img = Image.open(i)
	img = img.resize((width, height), Image.LANCZOS)
	img.save(i[:-4] + "_resized.jpg")
 