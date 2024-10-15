from fastapi import FastAPI
from auth_token import create_access_token, decode_token

app = FastAPI()
 
@app.get("/")
async def read_main():
    return {"msg": "Hello World"}

@app.get("/get_token")
async def create_token(name:str):
    token=create_access_token(name)
    return token

@app.get("/decode_token")
async def decode_tokens(name:str):
    token=decode_token(name)
    return token