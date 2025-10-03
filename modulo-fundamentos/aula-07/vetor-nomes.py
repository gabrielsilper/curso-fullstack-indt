import numpy as np

TAMANHO_VETOR = 5

vetor_nomes = np.empty(TAMANHO_VETOR, dtype=object)

for i in range(TAMANHO_VETOR):
    nome = input(f"Digite o {i + 1}º nome: ")
    vetor_nomes[i] = nome

for nome in vetor_nomes:
    if len(nome) > 5:
        print(nome)
