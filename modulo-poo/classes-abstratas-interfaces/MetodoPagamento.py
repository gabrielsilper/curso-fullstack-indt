from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

class PagamentoPix(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Pagando R${valor} via PIX instantâneo!")

class PagamentoCartao(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Pagando R${valor} com cartão de crédito.")

class PagamentoBoleto(MetodoPagamento):
    def processar_pagamento(self, valor):
        print(f"Pagando R${valor} com o boteto!")

def efetuar_pagamento(metodo: MetodoPagamento, valor):
    metodo.processar_pagamento(valor)

efetuar_pagamento(PagamentoPix(), 200)
efetuar_pagamento(PagamentoCartao(), 150)
efetuar_pagamento(PagamentoBoleto(), 320    )
