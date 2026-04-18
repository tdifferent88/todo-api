# To-Do API

API REST para gerenciamento de tarefas, desenvolvida com FastAPI e Python.

## Tecnologias
- Python 3.14
- FastAPI
- Uvicorn
- Pydantic

## Como rodar

```bash
# Clonar o projeto
git clone https://github.com/seu-usuario/todo-api

# Entrar na pasta
cd todo-api

# Criar e ativar o venv
python -m venv venv
venv\Scripts\activate

# Instalar dependências
pip install -r requirements.txt

# Rodar o servidor
uvicorn main:app --reload
```

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | /todos | Lista todas as tarefas |
| POST | /todos | Cria uma nova tarefa |
| GET | /todos/{id} | Busca uma tarefa pelo id |
| PUT | /todos/{id} | Atualiza uma tarefa |
| DELETE | /todos/{id} | Deleta uma tarefa |

## Documentação interativa

Após rodar o servidor, acesse:
http://localhost:8000/docs
