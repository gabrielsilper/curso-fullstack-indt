QTD_PARTIDAS = 5
QTD_TIMES = 4

partidas_times = []
times = []

for i in range(QTD_TIMES):
    time = input(f"Informe o nome do {i + 1}º time: ")
    times.append(time)


for time in times:
    partidas = []
    for i in range(QTD_PARTIDAS):
        gols = int(
            input(f"Informe quantos gols o time {time} fez na {i + 1}º partida: ")
        )
        partidas.append(gols)
    partidas_times.append(partidas)
    print()

times_proporcoes_maior = []

for i, time in enumerate(times):
    marcou_2_mais = 0
    for partida_gols in partidas_times[i]:
        if partida_gols >= 2:
            marcou_2_mais += 1
    proporcao = (marcou_2_mais / QTD_PARTIDAS) * 100
    print(f"O time {time} teve a proporção de {proporcao}%")
    if proporcao >= 60:
        times_proporcoes_maior.append(time)

print("\nTimes com proporção maior que 60%:")
for time in times_proporcoes_maior:
    print(time)
