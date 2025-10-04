# Restaurante (Cardápio ou Pedidos)
# Cada prato possui:
# Nome, Preço e Disponibilidade.
# Tarefas:
# Criar a classe Prato.
# Métodos:
# exibir() → mostra nome e preço.
# alterar_preco(novo_preco) → altera o valor do prato.
# indisponibilizar() → marca o prato como indisponível.


# Criar a classe Pedido que contém uma lista de pratos.
# Método:
# total() → soma o valor de todos os pratos no pedido.


class Prato:
    def __init__(self, nome: str, preco: float, disponibilidade: bool):
        self.nome = nome
        self.preco = preco
        self.disponibilidade = disponibilidade

    def __str__(self):
        return

    def exibir(self) -> None:
        print(
            f"""
        -- Prato --
        Nome: {self.nome}
        Preço: {self.preco}
        """
        )

    def alterar_preco(self, novo_preco: float) -> None:
        self.preco = novo_preco

    def indisponibilizar(self) -> None:
        self.disponibilidade = False


class Pedido:
    def __init__(self, pratos: list[Prato]):
        self.pratos = pratos

    def total(self) -> float:
        total = 0
        for prato in self.pratos:
            if prato.disponibilidade:
                total += prato.preco
        return total

if __name__ == "__main__":
    prato1 = Prato("Lasanha", 45, True)
    prato2 = Prato("Churrasco", 25, True)
    prato3 = Prato("Torta de Frango", 38, True)

    pedido = Pedido([prato1, prato2, prato3])

    print("O valor total do pedido é", pedido.total())

    prato3.indisponibilizar()

    print("O valor total do pedido é", pedido.total())