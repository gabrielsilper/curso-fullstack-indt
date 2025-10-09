class Veiculo:
    def __init__(self, marca: str = "Sem Marca Definida"):
        self.__marca = marca

    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca


class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str = "Sem Modelo Definido"):
        super().__init__(marca)
        self.__modelo = modelo

    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        self.__modelo = modelo

carro = Carro("Chevrolet", "Onix Plus LT")

print(carro.get_modelo())
print(carro.get_marca())
