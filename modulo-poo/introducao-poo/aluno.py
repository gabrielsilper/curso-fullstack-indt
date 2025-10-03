class Aluno:
    def __init__(self, nome: str, nota1: float, nota2: float):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2

    def calcularMedia(self) -> float:
        return (self.nota1 + self.nota2) / 2

    def showResultado(self) -> None:
        print(
            f"O aluno {self.nome} foi",
            "aprovado." if self.calcularMedia() >= 7 else "reprovado.",
        )

aluno1 = Aluno("Gabriel", 8.5, 9.5)
aluno2 = Aluno("Pereira", 6.5, 3.8)

aluno1.showResultado()
aluno2.showResultado()
