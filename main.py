from fastapi import FastAPI

app = FastAPI()
#      to get docs
#     http://127.0.0.1:8000/redoc
#   to reload automatically
#    fastapi dev main.py


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/home")
def read_home():
    print("Hello from home")
    return {"Hello": "Home"}
#   parameter
@app.get("/item/{item_id}")
def read_par(item_id:int):
    return {"id":item_id}
