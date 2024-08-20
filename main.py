from usuarios import *
from servicos import *

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Gerenciar Usuários")
        print("2. Gerenciar Serviços")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            menu_usuarios()
        elif escolha == "2":
            menu_servicos()
        elif escolha == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    carregar_usuarios_csv()
    carregar_servicos_csv()
    menu_principal()
