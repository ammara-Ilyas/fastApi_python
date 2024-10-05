from fastapi import FastAPI
from pydantic import BaseModel

#      to get docs
#     http://127.0.0.1:8000/redoc
#   to reload automatically
#    fastapi dev main.py


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app=FastAPI()

@app.post("/item")
def create_item(item:Item):
    return item