import csv
from utils import salvar_usuarios_csv, carregar_usuarios_csv

usuarios = {}

def registrar_usuario():
    user_id = len(usuarios) + 1
    username = input("Digite o nome de usuário: ")
    password = input("Digite a senha: ")
    role = input("Digite o nível de acesso (administrador, mestre, jogador): ").lower()

    usuarios[user_id] = {"username": username, "password": password, "role": role}
    salvar_usuarios_csv(usuarios)

def listar_usuarios():
    for user_id, user_data in usuarios.items():
        print(f"ID: {user_id} - Usuário: {user_data['username']} - Role: {user_data['role']}")

def atualizar_usuario():
    user_id = int(input("Digite o ID do usuário a ser atualizado: "))
    if user_id in usuarios:
        username = input("Novo nome de usuário: ")
        password = input("Nova senha: ")
        role = input("Novo nível de acesso: ").lower()
        usuarios[user_id] = {"username": username, "password": password, "role": role}
        salvar_usuarios_csv(usuarios)
    else:
        print("Usuário não encontrado.")

def remover_usuario():
    user_id = int(input("Digite o ID do usuário a ser removido: "))
    if user_id in usuarios:
        del usuarios[user_id]
        salvar_usuarios_csv(usuarios)
    else:
        print("Usuário não encontrado.")

def menu_usuarios():
    while True:
        print("\n--- Gerenciar Usuários ---")
        print("1. Registrar novo usuário")
        print("2. Listar usuários")
        print("3. Atualizar usuário")
        print("4. Remover usuário")
        print("5. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            registrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            atualizar_usuario()
        elif opcao == "4":
            remover_usuario()
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")
