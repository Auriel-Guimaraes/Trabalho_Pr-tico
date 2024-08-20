import csv
from utils import salvar_servicos_csv, carregar_servicos_csv

servicos = []

def adicionar_servico():
    servico_id = len(servicos) + 1
    nome = input("Digite o nome do serviço: ")
    preco = float(input("Digite o preço do serviço: "))
    descricao = input("Digite a descrição do serviço: ")
    servicos.append({"id": servico_id, "nome": nome, "preco": preco, "descricao": descricao})
    salvar_servicos_csv(servicos)

def listar_servicos():
    for servico in servicos:
        print(f"ID: {servico['id']} - Serviço: {servico['nome']} - Preço: R${servico['preco']:.2f} - Descrição: {servico['descricao']}")

def atualizar_servico():
    servico_id = int(input("Digite o ID do serviço a ser atualizado: "))
    for servico in servicos:
        if servico['id'] == servico_id:
            servico['nome'] = input("Novo nome do serviço: ")
            servico['preco'] = float(input("Novo preço do serviço: "))
            servico['descricao'] = input("Nova descrição do serviço: ")
            salvar_servicos_csv(servicos)
            break
    else:
        print("Serviço não encontrado.")

def remover_servico():
    servico_id = int(input("Digite o ID do serviço a ser removido: "))
    global servicos
    servicos = [servico for servico in servicos if servico['id'] != servico_id]
    salvar_servicos_csv(servicos)

def buscar_servico_por_nome():
    nome = input("Digite o nome do serviço que deseja buscar: ").lower()
    resultados = [servico for servico in servicos if nome in servico['nome'].lower()]
    if resultados:
        for servico in resultados:
            print(f"ID: {servico['id']} - Serviço: {servico['nome']} - Preço: R${servico['preco']:.2f}")
    else:
        print("Serviço não encontrado.")

def ordenar_servicos_por_nome():
    servicos_ordenados = sorted(servicos, key=lambda s: s['nome'].lower())
    for servico in servicos_ordenados:
        print(f"ID: {servico['id']} - Serviço: {servico['nome']} - Preço: R${servico['preco']:.2f}")

def ordenar_servicos_por_preco():
    servicos_ordenados = sorted(servicos, key=lambda s: s['preco'])
    for servico in servicos_ordenados:
        print(f"ID: {servico['id']} - Serviço: {servico['nome']} - Preço: R${servico['preco']:.2f}")

def menu_servicos():
    while True:
        print("\n--- Gerenciar Serviços ---")
        print("1. Adicionar novo serviço")
        print("2. Listar serviços")
        print("3. Atualizar serviço")
        print("4. Remover serviço")
        print("5. Buscar serviço por nome")
        print("6. Ordenar serviços por nome")
        print("7. Ordenar serviços por preço")
        print("8. Voltar ao Menu Principal")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_servico()
        elif opcao == "2":
            listar_servicos()
        elif opcao == "3":
            atualizar_servico()
        elif opcao == "4":
            remover_servico()
        elif opcao == "5":
            buscar_servico_por_nome()
        elif opcao == "6":
            ordenar_servicos_por_nome()
        elif opcao == "7":
            ordenar_servicos_por_preco()
        elif opcao == "8":
            break
        else:
            print("Opção inválida.")
