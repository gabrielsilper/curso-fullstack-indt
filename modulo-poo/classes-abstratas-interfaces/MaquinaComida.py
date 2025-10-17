from abc import ABC, abstractmethod

class MaquinaComida(ABC):
    def ligar(self):
        print("Máquina ligada!")

    @abstractmethod
    def preparar_prato(self):
        pass

class MaquinaTacaca:
    def preparar_prato(self):
        print("Preparando Tacacá com jambu!")

class MaquinaVatapa:
    def preparar_prato(self):
        print("Preparando Vatapá com camarão!")

tacaca = MaquinaTacaca()
vatapa = MaquinaVatapa()

tacaca.preparar_prato()
vatapa.preparar_prato()
