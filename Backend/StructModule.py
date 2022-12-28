import os

def GetStruct():
	TopPos = 'E:\\GithubProjects\\Graduate-Website\\Backend\\Files'
	TopDirs = os.listdir(TopPos)

	DirStruct = {}

	# print(TopDirs)
	for dir in TopDirs:
		Datas = os.listdir(f"{TopPos}\\{dir}")
		if len(Datas[0].split('.')) == 1:
			for dir2 in os.listdir(f"{TopPos}\\{dir}"):
				DirStruct[f"{dir}\\{dir2}"] = True
		else:
			DirStruct[dir] = True

	return DirStruct