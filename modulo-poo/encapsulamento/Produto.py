class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco

    def set_preco(self, valor: float):
        if valor > 0:
            self.__preco = valor
        else:
            print("Preço inválido!")

    def get_preco(self) -> float:
        return self.__preco


