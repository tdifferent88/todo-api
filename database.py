# Lista simples como banco de dados
# Em produção usaria PostgreSQL ou SQLite
todos_db = []

# Contador para gerar IDs únicos
counter = 0

def get_next_id():
    global counter
    counter += 1
    return counter
