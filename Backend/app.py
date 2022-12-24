from fastapi import FastAPI, Request
from starlette.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import uvicorn
import random
import json
from datetime import datetime
import os

app = FastAPI(docs_url="/documentation", redoc_url=None)

Password = ""
with open('./Password.txt', "r") as f:
	Password = f.readline()

FileSavePassword = ""
with open('./FileSavePassword.txt', "r") as f:
	FileSavePassword = f.readline()

AvailableTokens = {}
# 'Token' : IP or Date?

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
	'체육대회-영상' : True,
}

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

TokenStrings = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
TokenStringsLen = len(TokenStrings) - 1
def RandomToken():
	return "".join([TokenStrings[random.randint(0, TokenStringsLen)] for i in range(512)])


@app.get('/')
def a():
	return True

@app.get('/get/')
async def ReadImage(token: str, imgdir: str, imgnum : int):
	if AvailableTokens.get(token) == None:
		return False
	else:
		if DirStruct.get(imgdir) == None:
			return False
		else:
			Dir = DirStruct.get(imgdir)
			if Dir == True:
				Dir = imgdir
			Dir = f"./Files/{Dir}"
			try:
				return FileResponse(f'{Dir}/{os.listdir(Dir)[imgnum]}')
			except:
				return False

@app.get('/getcount/')
async def ReadImage(token: str, imgdir: str):
	if AvailableTokens.get(token) == None:
		return False
	else:
		if DirStruct.get(imgdir) == None:
			return False
		else:
			Dir = DirStruct.get(imgdir)
			if Dir == True:
				Dir = imgdir
			Dir = f"./Files/{Dir}"
			return len(os.listdir(Dir))

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
	uvicorn.run("app:app", host="0.0.0.0", port=7070, reload=True)