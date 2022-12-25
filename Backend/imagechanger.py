import os
import PIL.Image

MainPos = 'E:\\GithubProjects\\Graduate-Website\\Backend\\Files'
PastePos = 'E:\\GithubProjects\\Graduate-Website\\Backend\\SmallFiles'

DirStruct = {
	'기타' : True,
	'3-1반' : '에버랜드/3-1반',
	'3-2반' : '에버랜드/3-2반',
	'3-3반' : '에버랜드/3-3반',
	'3-4반' : '에버랜드/3-4반',
	'3-5반' : '에버랜드/3-5반',
	'3-6반' : '에버랜드/3-6반',
	'연극' : True,
	'졸업사진-촬영' : True,
	'체육대회(1)' : True,
	'체육대회(2)' : True,
	'체육대회(3)' : True,
	'체육대회(4)' : True,
	# '체육대회-영상' : True,
}

Dirs = list(map(lambda x : x if DirStruct[x]==True else DirStruct[x], DirStruct.keys()))
print(Dirs)

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
			print(Link, file)
			TargetImage = PIL.Image.open(Link+"\\"+file)

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