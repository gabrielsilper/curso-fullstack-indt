from collections import deque

QTD_MAX_PRATOS = 5

pratos = deque()

while True:
    print(
        """
    1 - Adicionar prato na pilha
    2 - Retirar prato do topo
    3 - Ver prato do topo
    4 - Sair
    """
    )

    opcao = int(input("Informe a ação que deseja realizar:"))

    if opcao == 4:
        print("Encerrando programa...")
        break
    elif opcao == 1:
        if len(pratos) == QTD_MAX_PRATOS:
            print(
                f"Você não pode adicionar mais de {QTD_MAX_PRATOS} na pilha. Tente retirar um.\n"
            )
            continue
        prato = input("\nInforme o nome do prato: ").strip()
        if not prato:
            print("Nome inválido!\n")
            continue
        pratos.append(prato)
    elif opcao == 2:
        if not pratos:
            print("Não há pratos na pilha.")
            continue
        pop = pratos.pop()
        print(f"{pop} removido da pilha.")
    elif opcao == 3:
        if not pratos:
            print("Não há pratos na pilha.")
            continue
        print(f"Prato do topo da pilha: ", pratos[-1])
    else:
        print("Opção inválida")
    print("Pilha de pratos atualmente: ", pratos)
