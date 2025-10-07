# atributos nome e nota privados
# set nota somente 0 e 10
# get dos atributos


class Aluno:
    def __init__(self, nome: str, nota: float):
        self.__nome = nome
        self.__nota = nota

    def set_nota(self, nota):
        if nota < 0 or nota > 10:
            print("Nota inválida")
            return
        self.__nota = nota

    def get_nome(self):
        return self.__nome

    def get_nota(self):
        return self.__nota


aluno1 = Aluno("Gabriel Pereira", 8)

aluno1.set_nota(12)
aluno1.set_nota(10)

print(aluno1.get_nota())
