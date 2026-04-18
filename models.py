# Pydantic valida os dados automaticamente
from pydantic import BaseModel
from typing import Optional

# Campos base da tarefa
class TodoBase(BaseModel):
    # obrigatório
    title: str
    # opcional
    description: Optional[str] = None
    # padrão não concluída

# Usando na criação (sem id)
class TodoCreate(TodoBase):
    pass

# Retornando pela API (com id)
class Todo(TodoBase):
    id: int

    class Config:
        orm_mode = True
