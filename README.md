# To-Do API

API REST para gerenciamento de tarefas, desenvolvida com FastAPI e Python.

## 🔗 URL Pública
https://todo-api-6fqa.onrender.com

## 📖 Documentação interativa
https://todo-api-6fqa.onrender.com/docs

## Tecnologias
- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- Pytest

## Como rodar localmente

```bash
git clone https://github.com/tdifferent88/todo-api
cd todo-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Endpoints

| Método | Rota | Descrição |
|--------|------|-----------|
| GET | / | Rota inicial |
| GET | /todos | Lista todas as tarefas |
| POST | /todos | Cria uma nova tarefa |
| GET | /todos/{id} | Busca uma tarefa pelo id |
| PUT | /todos/{id} | Atualiza uma tarefa |
| DELETE | /todos/{id} | Deleta uma tarefa |

## Testes

```bash
pytest test_main.py -v
```
