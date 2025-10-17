from abc import ABC, abstractmethod

class AnimalFalante(ABC):
    @abstractmethod
    def falar(self):
        pass

class Papagaio(AnimalFalante):
    def falar(self):
        print("Aaa Aaa O Papagaio tá falando Aaa Aaa")

class GatoFofoqueiro(AnimalFalante):
    def falar(self):
        print("O Gato está fofocando...")

papagaio = Papagaio()
gato = GatoFofoqueiro()

papagaio.falar()
gato.falar()
