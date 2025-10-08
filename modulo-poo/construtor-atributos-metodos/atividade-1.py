class Produto:
    def __init__(self, nome: str, preco: float):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Nome: {self.nome} - Preço: R$ {self.preco}"


class Pedido:
    def __init__(self, produto: Produto, qtd_produto: int = 1):
        self.produto = produto
        self.qtd_produto = qtd_produto

    def __str__(self):
        return (
            "-- Pedido --\n"
            f"Produto - {self.produto}\n"
            f"Quantidade: {self.qtd_produto}"
        )


class CarrinhoDeCompras:
    def __init__(self, pedidos: list[Pedido] = []):
        self.pedidos = pedidos

    def __len__(self):
        total_itens = 0
        for pedido in self.pedidos:
            total_itens += pedido.qtd_produto
        return total_itens

    def adicionar_pedido(self, pedido: Pedido):
        self.pedidos.append(pedido)

    def calcular_total(self) -> float:
        total = 0
        for pedido in self.pedidos:
            total += pedido.produto.preco * pedido.qtd_produto
        return total

    def remover_ultimo_pedido(self):
        self.pedidos.pop()

    def limpar(self):
        self.pedidos.clear()

    def mostrar(self):
        print("\n----- Carrinho -----")
        for id, pedido in enumerate(self.pedidos):
            print(pedido)
            print("ID:", id)
        print("--------------------")
        print("Qtd. Itens: ", len(self))
        print("Total Carrinho: R$", self.calcular_total())


if __name__ == "__main__":
    produto1 = Produto("Coca Cola 2L", 8.49)
    produto2 = Produto("Pepsi 2L", 7.00)
    produto3 = Produto("Soda 2L", 8.00)

    produtos_disponiveis = [produto1, produto2, produto3]

    carrinho = CarrinhoDeCompras()

while True:
    print(
        """
    1 - Ver produtos disponíveis
    2 - Adicionar produto ao carrinho
    3 - Remover produto do carrinho
    4 - Desfazer último pedido
    5 - Limpar carrinho
    6 - Ver valor total do Carrinho
    7 - Ver quantidade de itens no carrinho
    8 - Ver Carrinho completo
    9 - Sair
    """
    )

    opcao = int(input("Informe a ação que deseja realizar: "))

    match opcao:
        case 9:
            print("Saindo do Programa")
            break
        case 1:
            for i, produto in enumerate(produtos_disponiveis):
                print("-----------")
                print("ID: ", i)
                print(produto)
            continue
        case 2:
            id = int(input("Informe o ID do produto que quer adicionar ao carrinho: "))
            if id < 0 or id > len(produtos_disponiveis) - 1:
                print("ID de produto inválido!")
                continue

            produto = produtos_disponiveis[id]
            qtd = int(
                input(
                    f"Informe a quantidade do produto {produto.nome} que quer adicionar ao carrinho: "
                )
            )

            carrinho.adicionar_pedido(Pedido(produto, qtd))
            print("Produto adicionado ao carrinho com sucesso!")
            continue
        case 3:
            if not carrinho:
                print("Não há itens no carrinho para ser removidos.")
                continue

            id = int(input("Informe o ID do produto que quer adicionar ao carrinho: "))
            if id < 0 or id > len(carrinho.pedidos) - 1:
                print("ID de produto inválido!")
                continue

            pedido = carrinho.pedidos[id]
            qtd_remover = int(
                input(
                    f"Informe quantos itens de {pedido.produto.nome} deseja remover.\n(informe -1 para remover tudo): "
                )
            )

            if qtd_remover < -1:
                print("Quantidade informada é inválida")
            elif qtd_remover == -1 or pedido.qtd_produto <= qtd_remover:
                carrinho.pedidos.remove(pedido)
                print("Produto removido com sucesso do seu carrinho")
            else:
                pedido.qtd_produto -= qtd_remover
                print(
                    f"{qtd_remover} de {pedido.produto.nome} foram removidos do carrinho"
                )
        case 4:
            if not carrinho:
                print("Não há itens no carrinho para ser removidos.")
                continue

            pedido_pop = carrinho.pedidos.pop()
            print(f"{pedido_pop.produto.nome} foi removido do carrinho")
            continue
        case 5:
            if not carrinho:
                print("Não há itens no carrinho para ser removidos.")
                continue
            carrinho.limpar()
            print("Seu carrinho foi limpo!")
        case 6:
            print("\nO valor atual do seu carrinho é R$", carrinho.calcular_total())
            continue
        case 7:
            print(f"\nVocê tem {len(carrinho)} itens no seu carrinho!")
            continue
        case 8:
            carrinho.mostrar()
            continue
        case _:
            print("Opção inválida")
