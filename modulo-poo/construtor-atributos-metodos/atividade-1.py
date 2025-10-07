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

    def limpar_carrinho(self):
        self.pedidos = []

    def mostrar_carrinho(self):
        for pedido in self.pedidos:
            print(pedido)
        print("-------------------")
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
            
            qtd = int(input("Informe o ID do produto que quer adicionar ao carrinho: "))
            
            produto = produtos_disponiveis[id]

