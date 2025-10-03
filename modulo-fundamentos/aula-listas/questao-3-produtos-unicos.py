# O supermercado Extra deseja gerar um relatório de vendas sem
# produtos repetidos; escreva um programa que receba do usuário a
# lista de produtos vendidos no dia, crie uma nova lista sem repetição
# mantendo a ordem da primeira ocorrência, conte quantas vezes cada
# produto foi vendido e exiba os produtos únicos e a contagem de
# vendas.

produtos_contagem = []

while True:
    produto = input("Digite o nome do produto vendido, digite 'Parar' para encerrar: ")

    if produto.lower() == "Parar".lower():
        break

    encontrou = False
    for produto_contagem in produtos_contagem:
        if produto_contagem[0].lower() == produto.lower():
            produto_contagem[1] += 1
            encontrou = True
        break
    if not encontrou:
        produtos_contagem.append([produto, 1])

for produto_contagem in produtos_contagem:
    print(f"Vendas do produto {produto_contagem[0]}: ", produto_contagem[1])
