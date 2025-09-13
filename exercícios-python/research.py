entrevistados = int(input("Olá, sua pesquisa possui quantos entrevistados?\n"))

qtd_fast_food = 0
qtd_caseira = 0
qtd_vegetariana = 0
qtd_vegana = 0
qtd_outros = 0
horas_sono_fast_food = 0
vegetariana_atividade = 0
veganas = 0
soma_idade = 0
nao_pratica_atividade = 0

for i in range(1, entrevistados + 1):
    print(f"Informe o hábito alimentar principal do {i}º entrevistado")
    print("1- Fast-food | 2- Caseira | 3- Vegetariana | 4- Vegana | 5- Outros")
    opcao_alimentar = int(input("Digite a opção: "))

    print(f"O {i}º entrevistado pratica atividade física regularmente?")
    pratica_atividade = int(input(f"1- Sim | 2- Não: "))

    print(f"O {i}º entrevistado dorme quantas horas por noite?")
    horas_sono = int(input(f"Digite a quantidade: "))

    print(f"O {i}º entrevistado possui quantos anos?")
    idade = int(input(f"Digite a quantidade: "))

    print(f"Qual o gênero do {i}º entrevistado?")
    genero_opcao = input(f"Digite 1 para feminino, 2 para masculino e 3 para Outros: ")

    if opcao_alimentar == 1:
        qtd_fast_food += 1
        horas_sono_fast_food = horas_sono
    if opcao_alimentar == 2:
        qtd_caseira += 1
    if opcao_alimentar == 3:
        qtd_vegetariana += 1
        if pratica_atividade == 1:
            vegetariana_atividade += 1
    if opcao_alimentar == 4:
        qtd_vegana += 1
        if genero_opcao == 1:
            veganas += 1
    if opcao_alimentar == 5:
        qtd_outros += 1

    if pratica_atividade == 2:
        soma_idade += idade
        nao_pratica_atividade += 1

    print("Pessoas com hábito alimentar de Fast-food:", qtd_fast_food)
    print("Pessoas com hábito alimentar de Caseira:", qtd_caseira)
    print("Pessoas com hábito alimentar de Vegetariana:", qtd_vegetariana)
    print("Pessoas com hábito alimentar de Vegana:", qtd_vegana)
    print("Pessoas com hábito alimentar de Outros:", qtd_outros)

    print(
        "Média de horas sono de pessoas que comem Fast-food:",
        horas_sono_fast_food / qtd_fast_food,
    )

    print(
        "Pessoas vegetarianas que praticam atividades físicas:", vegetariana_atividade
    )

    print("Quantidades de veganas:", veganas)

    if(nao_pratica_atividade > 0):
        print("Média de idade das não praticantes de atividades:", soma_idade / nao_pratica_atividade)
    else:
        print("Não possui pessoas que não praticam atividades!")
