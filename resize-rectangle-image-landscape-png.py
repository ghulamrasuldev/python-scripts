from PIL import Image
import glob
import os
 
lst_imgs = [i for i in glob.glob("*.png")]

 
print(lst_imgs)
for i in lst_imgs:
	img = Image.open(i)
	width = 1920
	height = img.height / img.width * 1920
	img = img.resize((int(width), int(height)), Image.LANCZOS)
	img.save(i[:-4] + "_resized.png")
 