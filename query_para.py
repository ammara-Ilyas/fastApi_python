from fastapi import FastAPI

app = FastAPI()
#      to get docs
#     http://127.0.0.1:8000/redoc
#   to reload automatically
#    fastapi dev main.py

@app.get("/item/{item_id}")
def read_quer(item_id:int,name:str | None = "ram",age:int | None=25):
    if name:
       return({"item":item_id,"student":name,"age":age})
        
    return({"item":item_id})