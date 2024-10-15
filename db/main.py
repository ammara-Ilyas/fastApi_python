from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from crud import create_todo, get_todos,update_todo,delete_todo
import  models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/todo")
def create_todo_api(todo:schemas.TodoCreat,db:Session=Depends(get_db)):
    print(todo)
    return create_todo(db=db,todo=todo)

@app.get("/todo")
def get_todos_api(skip: int = 0, limit: int = 100,db:Session=Depends(get_db)):
    todos= get_todos(db=db,skip=skip, limit=limit)
    return todos

@app.put("/todo")
def update_todo_api(todo:schemas.TodoUpdate,db:Session=Depends(get_db)):
#   print("to api",todo)
  return update_todo(db=db,todo=todo)


@app.delete("/todo")
def delete_todo_api(todo:schemas.TodoDelete,db:Session=Depends(get_db)):
  return delete_todo(db=db,todo=todo)
      