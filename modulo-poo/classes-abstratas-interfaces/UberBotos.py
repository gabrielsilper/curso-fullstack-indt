from abc import ABC, abstractmethod


class VeiculoFluvial(ABC):
    def __init__(self, nome):
        self._nome = nome

    def ligar_motor(self):
        print(f"Motor do {self._nome} ligado!")

    @abstractmethod
    def navegar(self):
        pass


from abc import ABC, abstractmethod


class ServicoTransporte(ABC):
    @abstractmethod
    def transportar(self, passageiro, destino):
        pass


class BarcoSolar(VeiculoFluvial, ServicoTransporte):
    def __init__(self, nome):
        super().__init__(nome)

    def navegar(self):
        print(
            f"Barco {self._nome} está navegando a 80km/H as margens rio Amazonas usando energia solar."
        )

    def transportar(self, passageiro, destino):
        print(
            f"Barco {self._nome} está transportando com segurança e agilidade o passageiro {passageiro} até {destino}"
        )


class BotoAutonomo(VeiculoFluvial, ServicoTransporte):
    def __init__(self, nome):
        super().__init__(nome)

    def navegar(self):
        print(f"O Boto {self._nome} está navegando a 50km/H nadando.")

    def transportar(self, passageiro, destino):
        print(
            f"O Boto {self._nome} está transportando o passageiro {passageiro} até {destino}"
        )


barcoSolar = BarcoSolar("Viva a Luz")
botoAutonomo = BotoAutonomo("Orácio")

barcoSolar.navegar()
botoAutonomo.navegar()

barcoSolar.transportar("Gabriel", "Parintins")
botoAutonomo.transportar("Clenio", "Autazes")
