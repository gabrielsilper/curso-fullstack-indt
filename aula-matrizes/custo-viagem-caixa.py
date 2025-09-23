import numpy as np

TAMANHO_MATRIZ = 2

matriz_qtd_caixa = np.ones((TAMANHO_MATRIZ, TAMANHO_MATRIZ))
matriz_valor_caixa = np.ones((TAMANHO_MATRIZ, TAMANHO_MATRIZ))

for i in range(TAMANHO_MATRIZ):
    for j in range(TAMANHO_MATRIZ):
        qtd_caixa = int(
            input(
                f"Digite a quantidade de caixas enviadas do deposito {i} para a loja {j}: "
            )
        )
        matriz_qtd_caixa[i][j] = qtd_caixa

for i in range(TAMANHO_MATRIZ):
    for j in range(TAMANHO_MATRIZ):
        valor_caixa = float(
            input(f"Digite a o valor por caixa enviada do deposito {i} à loja {j}")
        )
        matriz_valor_caixa[i][j] = valor_caixa

custo_total = 0
vetor_custo_lojas = np.zeros(TAMANHO_MATRIZ)
for i in range(TAMANHO_MATRIZ):
    custo_deposito = 0
    for j in range(TAMANHO_MATRIZ):
        custo_rota = matriz_qtd_caixa[i][j] * matriz_valor_caixa[i][j]
        print(f"Custo da rota do deposito {i} à loja {j}: ", custo_rota)
        vetor_custo_lojas[j] += custo_rota
        custo_total += custo_rota
        custo_deposito += custo_rota
    print(f"Custo do deposito {i}", custo_deposito)

for i in range(TAMANHO_MATRIZ):
    print(f"Custo da loja {i}: ", vetor_custo_lojas[i])

print("Custo total: ", custo_total)
