from fastapi import FastAPI, HTTPException
from models import Todo, TodoCreate
from database import todos_db, get_next_id

app = FastAPI(title="To-Do API")

# GET / — rota inicial
@app.get("/")
def root():
    return {"message": "To-Do API funcionando!"}

# GET /todos — listar todas as tarefas
@app.get("/todos")
def list_todos():
    return todos_db

# POST /todos — criar nova tarefa
@app.post("/todos", status_code=201)
def create_todo(todo: TodoCreate):
    new_todo = Todo(id=get_next_id(), **todo.model_dump())
    todos_db.append(new_todo)
    return new_todo

# GET /todos/{id} — buscar uma tarefa pelo id
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(404, detail="Tarefa não encontrada")

# PUT /todos/{id} — atualizar uma tarefa
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated: TodoCreate):
    for i, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todos_db[i] = Todo(id=todo_id, **updated.model_dump())
            return todos_db[i]
    raise HTTPException(404, detail="Tarefa não encontrada")

# DELETE /todos/{id} — deletar uma tarefa
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todos_db.pop(i)
            return {"message": "Tarefa deletada"}
    raise HTTPException(404, detail="Tarefa não encontrada")
