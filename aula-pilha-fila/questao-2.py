from collections import deque as deque

historico = deque()

while True:
    print("""
    1 - Visitar Página
    2 - Voltar para página anterior
    3 - Mostrar página atual
    4 - Sair
    """)

    opcao = int(input("Informe a ação que deseja realizar:"))

    if opcao == 4:
        print("Encerrando programa...")
        break
    elif opcao == 1:
        url = input("\nInforme a página que deseja acessar: ")
        historico.append(url)
        print(f"Acessando {url}...\n")
    elif opcao == 2:
        if historico:
            historico.pop()
            print(f"Voltando para a página anterior...")
        else:
            print(f"Não existe nenhuma página no histórico")
    elif opcao == 3:
        if historico:
            print(f"Página Atual: ", historico[-1])
        else:
            print(f"Não existe nenhuma página no histórico")
    else:
        print("Opção inválida!")
