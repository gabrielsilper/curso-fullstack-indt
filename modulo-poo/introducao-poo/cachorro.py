class Cachorro:
    def __init__(self, nome: str, raca: str):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f"Au Au, o cachorro {self.nome} está latindo")

cachorro = Cachorro("Mel", "Chowchow")

cachorro.latir()
