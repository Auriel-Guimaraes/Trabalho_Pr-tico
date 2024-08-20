import csv

def salvar_usuarios_csv(usuarios):
    with open('data/usuarios.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "username", "password", "role"])
        for user_id, user_data in usuarios.items():
            writer.writerow([user_id, user_data["username"], user_data["password"], user_data["role"]])

def carregar_usuarios_csv():
    try:
        with open('data/usuarios.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                user_id = int(row["user_id"])
                carregar_usuarios_csv [user_id] = {
                    "username": row["username"],
                    "password": row["password"],
                    "role": row["role"]
                }
    except FileNotFoundError:
        pass

def salvar_servicos_csv(servicos):
    with open('data/servicos.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["id", "nome", "preco", "descricao"])
        for servico in servicos:
            writer.writerow([servico["id"], servico["nome"], servico["preco"], servico["descricao"]])

def carregar_servicos_csv():
    try:
        with open('data/servicos.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                carregar_servicos_csv .append({
                    "id": int(row["id"]),
                    "nome": row["nome"],
                    "preco": float(row["preco"]),
                    "descricao": row["descricao"]
                })
    except FileNotFoundError:
        pass
