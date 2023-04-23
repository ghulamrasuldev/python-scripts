from PIL import Image
import glob
import os
 
# FInding all JPG images in the folder  
lst_imgs = [i for i in glob.glob("*.png")]
print(lst_imgs)

# Your custom width and height
height  = 900
frameWidth = 1024
frameHeight = 1024

# Converting images
for i in lst_imgs:
	foreground = Image.open(i)
	width = foreground.width / foreground.height * height
	foreground = foreground.resize((int(width), height), Image.LANCZOS)
	background = Image.new(mode="RGBA", size=(frameWidth,frameHeight), color="white")
	x = (background.width - foreground.width) // 2
	y = (background.height - foreground.height) // 2
	background = Image.alpha_composite(
		Image.new("RGBA", background.size),
		background.convert('RGBA')
    )
	background.paste(
		foreground,
		(x,y),
		foreground
    )
	background.save(i[:-4] + "-resized.png")