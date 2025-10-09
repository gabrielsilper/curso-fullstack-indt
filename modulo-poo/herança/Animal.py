class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        print(f"O {self.nome} fez um som")

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome


class Cachorro(Animal):
    pass


rex = Cachorro("Rex")
rex.falar()
