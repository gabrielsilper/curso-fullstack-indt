palavra = input("Digite uma palavra: ").lower()

count = 0

for letra in palavra:
    if letra in "aeiou":
        count += 1

print(f"A palavra '{palavra}' possui {count} vogais.")
