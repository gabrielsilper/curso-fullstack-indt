from abc import ABC, abstractmethod

class PagamentoInterface(ABC):
    @abstractmethod
    def processar_pagamento(self, valor: float):
        pass

class PagamentoCartão(PagamentoInterface):
    def processar_pagamento(self, valor: float):
        print(f"Processando pagamento do valor R$ {valor} no cartão")

class PagamentoPix(PagamentoInterface):
    def processar_pagamento(self, valor: float):
        print(f"Processando pagamento do valor R$ {valor} via Pix")

def realizar_pagamento(metodoPagamento: PagamentoInterface, valor: float):
    metodoPagamento.processar_pagamento(valor)

realizar_pagamento(PagamentoCartão(), 120)
realizar_pagamento(PagamentoPix(), 240)
