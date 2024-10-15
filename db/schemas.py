from pydantic import BaseModel


class TodoCreat(BaseModel):
    text:str

class TodoUpdate(BaseModel):
    id:int
    text:str

class TodoDelete(BaseModel):
    id:int

class Config:
        orm_mode = True 
