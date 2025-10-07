class Conta:
    def __init__(self, titular: str, saldo: float, limite: float) -> None:
        self.__titular = titular
        self.__saldo = saldo
        self._limite = limite

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, valor):
        if valor >= 0:
            self.__saldo = valor

    def get_limite(self):
        return self._limite


class ContaManager:
    def __init__(self, conta: Conta) -> None:
        self.__conta = conta

    def atualizar_limite(self, valor: float) -> None:
        if valor >= 0:
            self.__conta._limite = valor


conta = Conta("Gabriel Pereira", 250, 100)

print(conta.get_limite())

manager = ContaManager(conta)
manager.atualizar_limite(200)

print(conta.get_limite())
