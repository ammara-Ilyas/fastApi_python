from jose import jwt


secret="I'm secret key"
Algorithm="HS256"
def create_access_token(subject:str):
   token = jwt.encode({'name': subject}, secret, algorithm=Algorithm)
   return {"token":token}

def decode_token(token:str):
    decode_token= jwt.decode(token, secret, algorithms=Algorithm)
    return {"decode_token":decode_token}