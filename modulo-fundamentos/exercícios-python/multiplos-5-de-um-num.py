num = int(input("Digite um número: "))

if num > 0:
    soma = 0
    for i in range(1, num + 1):
        if i % 5 == 0:
            soma += i
    print(f"A soma dos múltiplos de 5 até o {num} é", soma)
else:
    print("O numero informado precisa ser maior que 0.")
