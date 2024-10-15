from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from db.crud import create_todo, get_todos
from db.schemas import  models, Todo
from db.database import SessionLocal, engine

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
def create_todo_api(todo:Todo,db:Session=Depends(get_db)):
    return create_todo(db=db,todo=todo)

@app.get("/todo")
def get_todos_api(skip: int = 0, limit: int = 100,db:Session=Depends(get_db)):
    todos= get_todos(db=db,skip=skip, limit=limit)
    return todos