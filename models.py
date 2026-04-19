from sqlalchemy import Column, Integer, String, Boolean
from database import Base

# Representa a tabela "todos" no banco de dados
class Todo(Base):
    __tablename__ = "todos"

    # Colunas da tabela
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)        # obrigatório
    description = Column(String, nullable=True)   # opcional
    completed = Column(Boolean, default=False)    # padrão: não concluída
