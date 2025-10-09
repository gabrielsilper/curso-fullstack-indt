class Pessoa:
    def __init__(self, nome: str = None):
        self.nome = nome

    def falar(self):
        print(f"{self.nome} está falando")


class Professor(Pessoa):
    def __init__(self, nome, disciplina):
        super().__init__(nome)
        self.disciplina = disciplina

    def falar(self):
        print(f"Professor(a) {self.nome} está ensinando {self.disciplina}")

class Aluno(Pessoa):
    def __init__(self, nome, matricula):
        super().__init__(nome)
        self.matricula = matricula

    def falar(self):
        print(f"Aluno(a) {self.nome} {self.matricula} está aprendendo")

pessoa1 = Pessoa("Maria")
pessoa2 = Professor("Carlos", "Matemática")
pessoa3 = Aluno("Ana", 100012)

pessoa1.falar()
pessoa2.falar()
pessoa3.falar()
