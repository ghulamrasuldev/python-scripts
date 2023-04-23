from PIL import Image
import glob
import os
 
lst_imgs = [i for i in glob.glob("*.jpg")]

 
print(lst_imgs)
for i in lst_imgs:
	img = Image.open(i)
	height = 1080
	width = img.width / img.height * 1080
	img = img.resize((int(width), int(height)), Image.LANCZOS)
	img.save(i[:-4] + "_resized.jpg")
 