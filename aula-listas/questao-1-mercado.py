# QTD_PRODUTOS = 2

# lista_produtos = []

# for i in range(QTD_PRODUTOS):
#     produto_info = []
#     produto_info.append(input(f"Informe o nome do produto {i}: "))
#     produto_info.append(int(input(f"Informe a quantidade do produto {i}: ")))
#     lista_produtos.append(produto_info)

# for i, produto in enumerate(lista_produtos):
#     if produto[1] < 10:
#         produto[1] = "Estoque Baixo"
#     print(f"Produto {i}: ", produto[0])
#     print(f"QTD produto {i}: ", produto[1])

# Outra forma de fazer

QTD_PRODUTOS = 2

lista_produtos = []

for i in range(QTD_PRODUTOS):
    lista_produtos.append(
        [
            input(f"Informe o nome do produto {i}: "),
            int(input(f"Informe a quantidade do produto {i}: ")),
        ]
    )

for i, produto in enumerate(lista_produtos):
    if produto[1] < 10:
        produto[1] = "Estoque Baixo"
    print(f"Produto {i}: ", produto[0])
    print(f"QTD produto {i}: ", produto[1])
