import numpy as np

num = int(input("Digite um número: "))

vetor = np.random.randint(0, 51, 10)
maior = menor = vetor[0]
soma = 0
isPresente = False

for valor in vetor[1:]:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    if num == valor:
        isPresente = True
    soma += valor

print(vetor)
print("O maior número do vetor é", maior)
print("O menor número do vetor é", menor)
print("A soma de todos elementos do vetor é", soma)
print("O número que você digitou está presente na lista?", "Sim" if isPresente else "Não")
