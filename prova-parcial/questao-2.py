import numpy as np

produtos_existentes = 0
LIMITE_PRODUTOS = 2
vetores_produtos = np.empty(10, dtype=object)
vetores_quantidade = np.empty(10, dtype=object)

while True:
    print("--- Sistema de gestão de produto da Mercearia ---")

    print(
        """
    1. Inclusão de novo produto
    2. Alteração de quantidade
    3. Exclusão de produto
    4. Impressão dos produtos cadastrados
    5. Consulta por nome do produto
    6. Sair
    """
    )

    opcao = int(input("Informe a opção: "))

    if opcao == 6:
        print("Encerrando sistema...")
        break
    if opcao < 1 or opcao > 6:
        print("Opção inválida, reiniciando menu...")
        continue

    if opcao == 1:
        if produtos_existentes == LIMITE_PRODUTOS:
            print("Você não pode mais cadastrar produtos, tente excluir um produto.\n")
            continue

        nome_produto = input("Nome do produto: ")
        qtd_produto = int(input("Quantidade do produto: "))

        vetores_produtos[produtos_existentes] = nome_produto
        vetores_quantidade[produtos_existentes] = qtd_produto
        produtos_existentes += 1
        continue

    if opcao == 2:
        id_busca = int(input("Informe o id do produto: "))
        if id_busca < 0 or id_busca > produtos_existentes - 1:
            print("ID informado é inválido, reiniciando menu...\n")
            continue

        qtd_nova = int(input("Nova quantidade do produto: "))
        vetores_quantidade[id_busca] = qtd_nova
        continue

    if opcao == 3:
        id_busca = int(input("Informe o id do produto: "))
        if id_busca < 0 or id_busca > produtos_existentes - 1:
            print("ID informado é inválido, reiniciando menu...\n")
            continue

        for i in range(produtos_existentes):
            if i == id_busca:
                for j in range(i, produtos_existentes - 1):
                    vetores_produtos[j] = vetores_produtos[j + 1]
                    vetores_quantidade[j] = vetores_quantidade[j + 1]
                vetores_produtos[produtos_existentes - 1] = None
                vetores_quantidade[produtos_existentes - 1] = None
                produtos_existentes -= 1
                break

    if opcao == 4:
        print("--- Produtos Cadastrados ---")
        for i in range(produtos_existentes):
            print("ID:", i)
            print("Nome produto:", vetores_produtos[i])
            print("QTD. produto:", vetores_quantidade[i], end="\n\n")
        print("-----------------------------\n")
        continue

    if opcao == 5:
        nome_busca = input("Informe o nome para busca: ")
        encontrou = False
        for i in range(produtos_existentes):
            if nome_busca.lower() == vetores_produtos[i].lower():
                encontrou = True
                print("ID:", i)
                print("Nome produto:", vetores_produtos[i])
                print("QTD. produto:", vetores_quantidade[i], end="\n\n")
                print("-----------------------------\n")
                break
        if not encontrou:
            print("Produto não encontrado!!!\n")
