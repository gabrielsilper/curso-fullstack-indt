from collections import deque

pacientes = deque()

qtd_idosos = qtd_agendamentos = 0

while True:
    print(
        """
    1 - Adicionar paciente a fila
    2 - Atender próximo paciente
    3 - Consultar Próximo paciente
    4 - Sair
    """
    )

    opcao = int(input("Informe a ação que deseja realizar:"))

    if opcao == 4:
        break
    elif opcao == 1:
        nome = input("Informe o nome do paciente: ")
        idade = int(input("Informe a idade: "))
        agendamento = int(input("Paciente possui agendamento, 1 - SIM | 2 - NÂO: "))
        if idade >= 60:
            pacientes.insert(qtd_idosos, nome)
            qtd_idosos+= 1
            continue
        elif agendamento == 1:
            pacientes.insert(qtd_idosos + qtd_agendamentos, nome)
            qtd_agendamentos+1
        else:
            pacientes.append(nome)
        print(f"Paciente {nome} adicionado a fila.")
    elif opcao == 2:
        if not pacientes:
            print("Não há pacientes na fila.")
            continue
        if qtd_idosos > 0:
            qtd_idosos -= 1
        elif qtd_agendamentos > 0:
            qtd_agendamentos -= 1
        paciente = pacientes.popleft()
        print(f"Paciente {paciente} foi atendido.")
    elif opcao == 3:
        if not pacientes:
            print("Não há pacientes na fila.")
            continue
        paciente = pacientes.popleft()
        print(f"Paciente {paciente} foi atendido.")
    else:
        print("Opção inválida")
    print("Fila de pacientes: ", pacientes)

    
