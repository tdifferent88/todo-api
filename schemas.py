from pydantic import BaseModel
from typing import Optional

# Campos base da tarefa
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False

# Usado na criação (sem id)
class TodoCreate(TodoBase):
    pass

# Retornado pela API (com id)
class TodoResponse(TodoBase):
    id: int

    class Config:
        from_attributes = True
