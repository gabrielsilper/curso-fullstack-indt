from abc import ABC, abstractmethod

class ServicoEntrega(ABC):
    @abstractmethod
    def calcular_frete(self, peso, distancia):
        pass

class Correios(ServicoEntrega):
    def calcular_frete(self, peso, distancia):
        return peso * 1.5 + distancia * 0.2
    
class Transportadora(ServicoEntrega):
    def calcular_frete(self, peso, distancia):
        return peso * 2 + distancia * 0.15
    
def exibir_frete(servico: ServicoEntrega, peso, distancia):
    print(servico.calcular_frete(peso, distancia))

exibir_frete(Correios(), 10, 15)
exibir_frete(Transportadora(), 10, 15)
