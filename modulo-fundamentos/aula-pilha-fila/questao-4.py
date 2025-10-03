from collections import deque

clientes = deque()
qtd_idosos = 0

while True:
    print(
        """
    1 - Adicionar cliente
    2 - Atender cliente
    3 - Ver próximo cliente
    4 - Sair
    """
    )

    opcao = int(input("Informe a ação que deseja realizar: "))

    if opcao == 4:
        print("Encerrando programa...")
        break
    elif opcao == 1:
        nome = input("Informe o nome do cliente: ")
        idade = int(input("Informe a idade: "))
        if idade >= 60 and qtd_idosos > 0:
            clientes.insert(qtd_idosos, nome)
            qtd_idosos += 1
        elif idade >= 60:
            clientes.appendleft(nome)
            qtd_idosos += 1
        else:
            clientes.append(nome)
        print(f"\nCliente {nome} adicionado à fila.")
    elif opcao == 2:
        if not clientes:
            print("Não há clientes na fila")
            continue
        if qtd_idosos > 0:
            qtd_idosos -= 1
        cliente = clientes.popleft()
        print(f"Cliente {cliente} foi atendido.")
    elif opcao == 3:
        if not clientes:
            print("Não há clientes na fila")
            continue
        print(f"Cliente {clientes[0]} é o próximo a ser atendido.")
    else:
        print("Opção inválida")
    print("Fila de clientes: ", clientes)
