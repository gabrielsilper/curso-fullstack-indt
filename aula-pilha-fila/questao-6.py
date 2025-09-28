from collections import deque

pacotes = deque()

qtd_urgentes = qtd_leves = qtd_pesados = 0

while True:
    print(
        """
    1 - Adicionar pacote a fila
    2 - Expedir próximo pacote
    3 - Consultar Próximo pacote
    4 - Sair
    """
    )

    opcao = int(input("Informe a ação que deseja realizar: "))

    if opcao == 4:
        print("Encerrando programa...")
        break
    elif opcao == 1:
        codigo = input("Informe o código do pacote: ")
        peso = int(input("Informe o peso do pacote(kg): "))
        urgente = int(input("O pacote é urgente? 1- SIM | 2- NÂO: ")) == 1

        if urgente:
            pacotes.insert(qtd_urgentes, codigo)
            qtd_urgentes += 1
        elif peso <= 5:
            pacotes.insert(qtd_urgentes + qtd_leves, codigo)
            qtd_leves += 1
        elif peso > 20:
            pacotes.insert(qtd_urgentes + qtd_leves + qtd_pesados, codigo)
            qtd_pesados += 1
        else:
            pacotes.append(codigo)
        print(f"Pacote {codigo} foi adicionado à fila.")
    elif opcao == 2:
        if not pacotes:
            print("Não há pacotes na fila.")
            continue
        if qtd_urgentes > 0:
            qtd_urgentes -= 1
        elif qtd_leves > 0:
            qtd_leves -= 1
        elif qtd_pesados > 0:
            qtd_pesados -= 1
        
        codigo = pacotes.popleft()
        print(f"O Pacote {codigo} foi expedido.")
    elif opcao == 3:
        if not pacotes:
            print("Não há pacotes na fila.")
            continue
        print(f"O Pacote {pacotes[0]} é o próximo.")
    else:
        print("Opção inválida")
    print("Fila dos pacotes: ", pacotes)
