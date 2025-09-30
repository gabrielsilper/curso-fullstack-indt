import numpy as np
from collections import deque

QTD_LOJAS = QTD_DEPOSITOS = 3

matriz_custo = np.zeros((QTD_LOJAS, QTD_DEPOSITOS))
matriz_capacidade_max = np.zeros((QTD_LOJAS, QTD_DEPOSITOS))
matriz_qtd_caixas_expedidas = np.zeros((QTD_LOJAS, QTD_DEPOSITOS))

print("Seção de Cadastro das rotas")
for i in range(QTD_DEPOSITOS):
    for j in range(QTD_LOJAS):
        custo = float(
            input(
                f"Digite o custo da entrega do depósito {i + 1} para a loja {j + 1}: "
            )
        )
        qtd_max = int(
            input(
                f"Digite a capacidade máxima de caixa do depósito {i + 1} para a loja {j + 1}: "
            )
        )
        matriz_custo[i][j] = custo
        matriz_capacidade_max[i][j] = qtd_max

pedidos = deque()
pedidos_expedidos = deque()
qtd_urgentes = qtd_leves = qtd_pesados = 0

while True:
    print(
        "\nSeção de Cadastro de pedidos, para encerrar os cadastros digite 'Sair' no código do produto"
    )
    codigo = input("Informe o código do produto: ")

    if codigo.lower() == "sair":
        break

    urgencia = (
        input("Informe a urgência do pedido, U - Urgente | N - Normal: ").lower()
        == "U".lower()
    )
    peso = float(input("Informe o peso do produto(kg): "))
    qtd_caixas = int(input("Informe a quantidade de caixas do pedido: "))
    deposito = int(input("Informe o depósito, 1 - D1 | 2 - D2 | 3 - D3: "))
    loja = int(input("Informe a loja, 1 - L1 | 2 - L2 | 3 - L3: "))
    custo_estimado = matriz_custo[deposito - 1][loja - 1] * qtd_caixas
    possui_risco = peso > 20 or qtd_caixas > 100

    pedido = [
        codigo,
        urgencia,
        peso,
        qtd_caixas,
        deposito,
        loja,
        custo_estimado,
        possui_risco,
    ]

    if urgencia:
        pedidos.insert(qtd_urgentes, pedido)
        qtd_urgentes += 1
    elif peso <= 5:
        pedidos.insert(qtd_urgentes + qtd_leves, pedido)
    elif peso >= 20:
        pedidos.insert(qtd_urgentes + qtd_leves + qtd_pesados, pedido)
    else:
        pedidos.append(pedido)

while True:
    print(
        """
    1 - Expedir próximo pedido
    2 - Consultar próximo pedido
    3 - Desfazer ultima expedição
    4 - Relatórios
    5 - Sair
    """
    )

    opcao = int(input("Informe a ação que deseja realizar:"))

    if opcao == 5:
        print("Encerrando programa...")
        break
    elif opcao == 1:
        if not pedidos:
            print("Não há pedidos na fila.")
            continue
        if qtd_urgentes > 0:
            qtd_urgentes -= 1
        elif qtd_leves > 0:
            qtd_leves -= 1
        elif qtd_pesados > 0:
            qtd_pesados -= 1

        expedido = pedidos.popleft()
        if expedido[3] > matriz_capacidade_max[expedido[4] - 1, expedido[5] - 1]:
            print(
                "Pedido possui quantidade de caixa maior que capacidade da rota! Pedido adiado!"
            )
            pedidos.append(expedido)
            continue
        matriz_qtd_caixas_expedidas[expedido[4] - 1, expedido[5] - 1] += expedido[3]
        pedidos_expedidos.append(expedido)
        print(f"Pedido {expedido} foi expedido.")

    elif opcao == 2:
        if not pedidos:
            print("Não há pedidos na fila.")
            continue
        print("O próximo pedido é: ", pedidos[0])
    elif opcao == 3:
        if not pedidos_expedidos:
            print("Não há pedidos para serem desfeitos")
            continue
        pedido_desfeito = pedidos_expedidos.pop()
        matriz_qtd_caixas_expedidas[
            pedido_desfeito[4] - 1, pedido_desfeito[5] - 1
        ] -= pedido_desfeito[3]
        pedidos.append(pedido_desfeito)
        print(f"O pedido {pedido_desfeito} voltou para o final da fila.")
    elif opcao == 4:
        if not pedidos_expedidos:
            print("Não há pedidos expedidos para gerar relatórios")
            continue
        custo_por_rota = matriz_custo * matriz_qtd_caixas_expedidas
        print("\nCusto por rota (matriz 3×3): ", custo_por_rota)
        print("Custo por deposito (vetor de 3): ", np.sum(custo_por_rota, axis=1))
        print("Custo por loja (vetor de 3): ", np.sum(custo_por_rota, axis=0))
        print("Custo total: ", np.sum(custo_por_rota))
        urgentes = normais = riscos = 0
        for expedido in pedidos_expedidos:
            if expedido[1]:
                urgentes += 1
            else:
                normais += 1

            if expedido[-1]:
                riscos += 1
        print("Quantos pedidos urgentes: ", urgentes)
        print("Quantos pedidos normais: ", normais)
        print("Quantos pedidos com risco: ", riscos)
    else:
        print("Opção inválida")
