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
            input(f"Digite a o valor por caixa enviada do deposito {i} à loja {j}: ")
        )
        matriz_valor_caixa[i][j] = valor_caixa

matriz_total = matriz_qtd_caixa * matriz_qtd_caixa

custo_total = np.sum(matriz_total)

print(matriz_total)

custo_deposito = np.sum[matriz_total, 0]
for i in range(TAMANHO_MATRIZ):
    for j in range(TAMANHO_MATRIZ):
        print(f"Custo da rota do deposito {i} à loja {j}: ", matriz_total[i,j])

custo_loja = np.sum[matriz_total, 1]
for i in range(TAMANHO_MATRIZ):
    print(f"Custo da loja {i}", custo_loja)

print("Custo total: ", custo_total)
