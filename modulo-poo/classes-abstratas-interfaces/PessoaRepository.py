from Pessoa import Pessoa
from IRepository import IRepository


class PessoaRepository(IRepository):

    def __init__(self):
        super().__init__("Pessoas")
        self.__listaPessoa: list[Pessoa] = []
        self.__currentId = 0

    def save(self, pessoa: Pessoa):
        self.__currentId += 1
        pessoa.id = self.__currentId
        self.__listaPessoa.append(pessoa)

    def findAll(self):
        return self.__listaPessoa

    def findById(self, id: int):
        for pessoa in self.__listaPessoa:
            if pessoa.id == id:
                return pessoa

    def countAll(self):
        return len(self.__listaPessoa)
