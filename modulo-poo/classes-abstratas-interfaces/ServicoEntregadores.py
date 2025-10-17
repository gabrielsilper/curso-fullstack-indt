from abc import ABC, abstractmethod

class ServicoEntrega(ABC):
    @abstractmethod
    def entregar(self, pedido):
        pass

class EntregaDeCanoa:
    def entregar(self, pedido):
        print(f"Entregando {pedido} pelo rio Negro!")

class EntregaDeMoto:
    def entregar(self, pedido):
        print(f"Entregando {pedido} pelo trânsito de Manaus!")


def realizar_entrega(servico: ServicoEntrega, pedido):
    servico.entregar(pedido)

realizar_entrega(EntregaDeCanoa(), "2 tubos de aço")
realizar_entrega(EntregaDeMoto(), "Calça Jeans")

