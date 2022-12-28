from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn
import random
import json
from datetime import datetime
import os
from StructModule import GetStruct

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
	CORSMiddleware,
	allow_origins=origins,
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"]
)

Password = ""
with open('./Password.txt', "r") as f:
	Password = f.readline()

FileSavePassword = ""
with open('./FileSavePassword.txt', "r") as f:
	FileSavePassword = f.readline()

AvailableTokens = {'6Bi8uhpvXuEEydZtcif5JF4zSE7bF0yAms7EpT2BQycdlNG6o2zXK8JYSZuNp8wQgJ2fYMbnddWoJaohSvr0yCR1uTiGyEq1ZlwdIVEwsbAs2DK4gUfP5QkPVX3PVJWcRVYtO2hOohp9MJSjCAOzXf2dGA2b29WzSaDuOB2mCJT1asY6QMMH5kp0tt5BDo11kwaSQ4C8nhDa180a0tND8KMQN11SlNHMCssAtAxnvdGyeqITHtpOUwfLYNWRcg4ei5wO5ZIidb331DEwdRBFKfNZPLaY5efj5DJjScZJBkQuGGpkfGVp3WrzqGiejihuI1FdxKFUXqczB0awi9NZKFE1y7XXV9UNtUQ24BsDRFGpLDNhcZT2OcGLzHBLbUCKwNTKMz641NYlOuMfHJGW0d2K9N8wo2XqdOCs7KT9qryolAtL1zm2Irz71t9UZi1lGZKqagPW8nfmIRWvAaZvyQ2dEI5TUZI6mc4I4XyPFrexKDnxkDZFYEMCDNPGDhpP' : True}
# 'Token' : IP or Date?

DirStructOld = GetStruct()
DirStruct={}
for key,value in DirStructOld.items():
	if "\\" in key:
		key = str(key).replace('\\','_')
	DirStruct[key] = True


TokenStrings = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
TokenStringsLen = len(TokenStrings) - 1
def RandomToken():
	return "".join([TokenStrings[random.randint(0, TokenStringsLen)] for i in range(512)])


@app.get('/')
def a():
	return True

@app.get('/getstruct/')
def a():
	return DirStruct

@app.get('/get/')
async def ReadImage(token: str, imgdir: str, imgnum : int, isoriginal : bool = False):
	if AvailableTokens.get(token) == None:
		return False
	else:
		if DirStruct.get(imgdir) == None:
			return False
		else:
			TempDir = str(imgdir).replace('_',"\\")
			if isoriginal:
				Dir = f"./Files/{TempDir}"
			else:
				Dir = f"./SmallFiles/{TempDir}"
			if str(imgdir)[0] == "V":
				Dir = f"./Files/{TempDir}"
				if not isoriginal:
					try:
						return os.listdir(Dir)[imgnum]
					except:
						return "존재하지 않는 데이터입니다."
				# return FileResponse(f"./Video-SmallFile.png")
			print(Dir)
			try:
				print(f'{Dir}/{os.listdir(Dir)[imgnum]}')
				return FileResponse(f'{Dir}/{os.listdir(Dir)[imgnum]}')
			except:
				return "존재하지 않는 데이터입니다"

@app.get('/getcount/')
async def ReadImage(token: str, imgdir: str):
	if AvailableTokens.get(token) == None:
		return False
	else:
		if DirStruct.get(imgdir) == None:
			return False
		else:
			Dir = str(imgdir).replace('_',"\\")
			if Dir == True:
				Dir = imgdir
			Dir = f"./Files/{Dir}"
			try:
				return len(os.listdir(Dir))
			except:
				return False

Struct = []

# @app.get('/getstruct/')
# def GetStruct():
# 	return DirStruct

@app.get('/gettoken/')
def GetToken(pw : str):
	if Password == pw:
		Token = RandomToken()
		AvailableTokens[Token] = datetime.now().strftime("%Y%m%d")
		return {"Token" : Token}
	else:
		return False

@app.get('/savefiles/')
def SaveFiles(pw : str):
	if FileSavePassword == pw:
		with open("Tokens.txt","w") as f:
			f.write(json.dumps(AvailableTokens))
		return True
	else:
		return False

if __name__ == "__main__":
	uvicorn.run("app:app", host="0.0.0.0", port=999, reload=True)