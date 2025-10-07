class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco

    def set_preco(self, valor: float):
        if valor >= 0:
            self.__preco = valor
        else:
            print("Preço inválido!")

    def get_nome(self):
        return self.__nome

    def get_preco(self) -> float:
        return self.__preco
    
produto1 = Produto("Coca cola lata", 4)
produto2 = Produto("Bolacha água e sal", 7)

produto1.set_preco(-12)
produto1.set_preco(3.5)

print(produto1.get_preco())

produto2.__preco = 23

print(produto2.get_preco())
