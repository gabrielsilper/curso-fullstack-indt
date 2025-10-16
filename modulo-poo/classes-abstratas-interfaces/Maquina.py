from abc import ABC, abstractmethod

class Maquina(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Liquidificador(Maquina):
    def ligar(self):
        print("Ligando o liquidificador... Bzzzz!")

class Computador(Maquina):
    def ligar(self):
        print("Iniciando o sistema operacional!")

l = Liquidificador()
c = Computador()

l.ligar()
c.ligar()
