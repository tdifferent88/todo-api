from fastapi.testclient import TestClient
from main import app

# Cliente de teste do FastAPI
client = TestClient(app)

# Testa a rota inicial
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "To-Do API funcionando!"}

# Testa a criação de uma tarefa
def test_create_todo():
    response = client.post("/todos", json={
        "title": "Tarefa de teste",
        "description": "Testando a criação",
        "completed": False
    })
    assert response.status_code == 201
    assert response.json()["title"] == "Tarefa de teste"
    assert response.json()["completed"] == False

# Testa a listagem de tarefas
def test_list_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Testa buscar uma tarefa pelo id
def test_get_todo():
    # Primeiro cria uma tarefa
    create = client.post("/todos", json={
        "title": "Buscar essa tarefa",
        "description": "Teste de busca",
        "completed": False
    })
    todo_id = create.json()["id"]

    # Depois busca pelo id
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["id"] == todo_id

# Testa atualizar uma tarefa
def test_update_todo():
    # Cria uma tarefa
    create = client.post("/todos", json={
        "title": "Atualizar essa tarefa",
        "description": "Antes da atualização",
        "completed": False
    })
    todo_id = create.json()["id"]

    # Atualiza a tarefa
    response = client.put(f"/todos/{todo_id}", json={
        "title": "Tarefa atualizada",
        "description": "Depois da atualização",
        "completed": True
    })
    assert response.status_code == 200
    assert response.json()["completed"] == True
    assert response.json()["title"] == "Tarefa atualizada"

# Testa deletar uma tarefa
def test_delete_todo():
    # Cria uma tarefa
    create = client.post("/todos", json={
        "title": "Deletar essa tarefa",
        "description": "Será deletada",
        "completed": False
    })
    todo_id = create.json()["id"]

    # Deleta a tarefa
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Tarefa deletada"}

    # Confirma que não existe mais
    response = client.get(f"/todos/{todo_id}")
    assert response.status_code == 404

# Testa buscar tarefa inexistente
def test_get_todo_not_found():
    response = client.get("/todos/99999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Tarefa não encontrada"}
