import numpy as np

TAMANHO_VETOR = 8
vetor_temperatura = np.empty(8, dtype=int)
soma = soma_fahrenheit = 0

for i in range(TAMANHO_VETOR):
    vetor_temperatura[i] = int(input(f"Digite o valor da {i+1}º temperatura: "))

maior = menor = vetor_temperatura[0]

for i in range(TAMANHO_VETOR):
    temp = vetor_temperatura[i]
    soma += temp
    vetor_temperatura[i] = temp * 1.8 + 32
    if temp > maior:
        maior = temp
    if temp < menor:
        menor = temp

media_temp = soma / TAMANHO_VETOR

print("Vetor convertido para Fahrenheit: ", vetor_temperatura)
print("A temperatura média em Celsius é", media_temp)
print("A temperatura média em Fahrenheit é", media_temp * 1.8 + 32)
print(
    f"A temperatura mínima em celsius é {menor} que em fahrenheit é {(menor * 1.8) + 32}"
)
print(
    f"A temperatura máxima em celsius é {maior} que em fahrenheit é {(maior * 1.8) + 32}"
)
