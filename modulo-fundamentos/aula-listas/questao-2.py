QTD_PARTIDAS = 2
QTD_TIMES = 2

proporcoes_times = []

for i in range(QTD_TIMES):
    time = input(f"Informe o nome do {i + 1}º time: ")
    marcou_2_mais = 0
    for j in range(QTD_PARTIDAS):
        gols = int(
            input(f"Informe quantos gols o time {time} fez na {i + 1}º partida: ")
        )
        if gols >= 2:
            marcou_2_mais += 1
    proporcoes_times.append([time, (marcou_2_mais / QTD_PARTIDAS) * 100])


for proporcao_time in proporcoes_times:
    print(f"O time {proporcao_time[0]} teve a proporção de {proporcao_time[1]}%")

print("\nTimes com proporção maior que 60%:")
for proporcao_time in proporcoes_times:
    if proporcao_time[1] >= 60:
        print(proporcao_time)
