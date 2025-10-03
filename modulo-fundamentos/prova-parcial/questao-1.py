qtd_onibus = qtd_carro = qtd_moto = qtd_bicicleta = qtd_outros = 0
gasto_mensal_bicicleta = 0
qtd_znorte_outros = qtd_zsul_carro = 0
soma_idade_feminino = qtd_feminino_onibus = 0


while True:
    print("Qual o meio de transporte principal?")
    print("1 - Ônibus | 2 - Carro | 3 - Moto | 4 - Bicicleta | 5 - Outros")
    transporte = int(input("Digite a opção: "))

    if transporte == 0:
        break
    elif transporte < 0 or transporte > 5:
        print("Opção inválida, reiniciando menu...")
        continue

    print("Qual a zona de moradia?")
    print("1 - Zona Norte | 2 - Zona Sul | 3 - Outros")
    zona = int(input("Digite a opção: "))

    if zona < 1 or zona > 3:
        print("Opção inválida, reiniciando menu...")
        continue

    gasto_mensal = float(input("Gasto mensal com transporte (R$): "))

    idade = int(input("Idade: "))

    print("Qual o genero do participante?")
    print("1 - Feminino | 2 - Masculino | 3 - Outro")
    genero = int(input("Digite a opção: "))
    if genero < 1 or genero > 3:
        print("Opção inválida, reiniciando menu...")
        continue

    if transporte == 1:
        qtd_onibus += 1
        if genero == 1:
            soma_idade_feminino += idade
            qtd_feminino_onibus += 1
    if transporte == 2:
        qtd_carro += 1
        if zona == 2:
            qtd_zsul_carro += 1
    if transporte == 3:
        qtd_moto += 1
    if transporte == 4:
        qtd_bicicleta += 1
        gasto_mensal_bicicleta += gasto_mensal
    if transporte == 5:
        qtd_outros += 1
        if zona == 1:
            qtd_znorte_outros += 1


print("Quantidade de participantes por ônibus:", qtd_onibus)
print("Quantidade de participantes por carro:", qtd_carro)
print("Quantidade de participantes por moto:", qtd_moto)
print("Quantidade de participantes por bicicleta:", qtd_bicicleta)
print("Quantidade de participantes por outros:", qtd_outros)

if qtd_bicicleta > 0:
    print(
        "Média de gasto mensal de quem anda de bicicleta:",
        gasto_mensal_bicicleta / qtd_bicicleta,
    )
else:
    print("Não teve participante com meio de transporte bicicleta")

print(
    "O número de pessoas da Zona Norte que usam Outros transportes: ", qtd_znorte_outros
)
print("O número de pessoas da Zona Sul que usam Carro: ", qtd_zsul_carro)

if qtd_feminino_onibus > 0:
    print(
        "A média de idade das mulheres que usam Ônibus: ",
        soma_idade_feminino / qtd_feminino_onibus,
    )
else:
    print("Não teve participante femininas usando onibus")
