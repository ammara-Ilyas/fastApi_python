from sqlalchemy.orm import Session
from schemas import  TodoCreat,TodoUpdate,TodoDelete
from models import Todo


def get_todo(db: Session, id: int):
    return db.query(Todo).filter(Todo.id == id).first()

def get_todos(db: Session,skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()

def create_todo(db:Session,todo:TodoCreat):
    print(todo)
    todo=Todo(text=todo.text)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return "Todo has been created"

def update_todo(db:Session,todo:TodoUpdate):
    print(todo.id)
    filter_todo=db.query(Todo).filter(Todo.id == todo.id).first()
    if filter_todo:
     filter_todo.text=todo.text
     db.add(filter_todo)
     db.commit()
     db.refresh(filter_todo)
     return f"Todo {todo.id} has been updated"
 
    return "No todo"


def delete_todo(db:Session,todo:TodoDelete):
    print("id",todo.id)
    filter_todo=db.query(Todo).filter(Todo.id == todo.id).first()
    if filter_todo:
     db.delete(filter_todo)
     db.commit()
     return f"Todo {todo.id} has been deleted "
 
    return "No todo"