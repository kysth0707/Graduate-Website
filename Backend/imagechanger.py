import os
import PIL.Image
from StructModule import GetStruct
import cv2

MainPos = 'E:\\GithubProjects\\Graduate-Website\\Backend\\Files'
PastePos = 'E:\\GithubProjects\\Graduate-Website\\Backend\\SmallFiles'

DirStruct = GetStruct()

# Dirs = list(map(lambda x : x if DirStruct[x]==True else DirStruct[x], DirStruct.keys()))
Dirs = list(DirStruct.keys())
# print(Dirs)

BackgroundImagePos = "E:\\GithubProjects\\Graduate-Website\\Backend\\Background.png"

def TryDivide(TargetImageSize):
	x,y=0,0
	try:
		x=int((256 - TargetImageSize[0])/2)
	except:
		pass
	try:
		y=int((256 - TargetImageSize[1])/2)
	except:
		pass
	return (x,y)

for x in Dirs:
	Link = f"{MainPos}\\{x}"
	Files = os.listdir(Link)
	for file in Files:
		try:
			width, height = TargetImage.size
			NewHeight, NewWidth = 256, 256
			if width > height:
				# width
				# newwidth : newheight = width : height
				# 256 : x = width : height
				# x * width = 256 * height
				# x = 256*height/width
				NewHeight = int(256 * height / width)
			else:
				# height
				# newwidth : newheight = width : height
				# x : 256 = width : height
				# 256 * width = x * height
				# x = 256 * width / height
				NewWidth = int(256 * width / height)

			TargetImage = TargetImage.resize((NewWidth, NewHeight))
			BackgroundImage = PIL.Image.open(BackgroundImagePos)

			BackgroundImage.paste(TargetImage, (TryDivide(TargetImage.size)))
			BackgroundImage.save(f"{PastePos}\\{x}\\{file}")
		except:
			BackgroundImage = PIL.Image.open(BackgroundImagePos)
			BackgroundImage.save(f"{PastePos}\\{x}\\{file}")
			print(f'Fail. {x}\\{file}')
			