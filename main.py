from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import engine, get_db, Base
from models import Todo
from schemas import TodoCreate, TodoResponse

# Cria as tabelas no banco automaticamente ao iniciar
Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-Do API")

# GET / — rota inicial
@app.get("/")
def root():
    return {"message": "To-Do API funcionando!"}

# GET /todos — listar todas as tarefas
@app.get("/todos")
def list_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()

# POST /todos — criar nova tarefa
@app.post("/todos", status_code=201, response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    new_todo = Todo(**todo.model_dump())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

# GET /todos/{id} — buscar uma tarefa pelo id
@app.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(404, detail="Tarefa não encontrada")
    return todo

# PUT /todos/{id} — atualizar uma tarefa
@app.put("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, updated: TodoCreate, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(404, detail="Tarefa não encontrada")
    todo.title = updated.title
    todo.description = updated.description
    todo.completed = updated.completed
    db.commit()
    db.refresh(todo)
    return todo

# DELETE /todos/{id} — deletar uma tarefa
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(404, detail="Tarefa não encontrada")
    db.delete(todo)
    db.commit()
    return {"message": "Tarefa deletada"}
