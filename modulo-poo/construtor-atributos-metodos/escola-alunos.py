# Uma escola precisa organizar os alunos que estão matriculados.
# Cada aluno tem um nome, idade e curso. A escola, por sua vez, deve ter uma lista de alunos matriculados.
# Desenvolva as classes necessárias para que seja possível adicionar novos alunos à escola e listar todos os alunos cadastrados.
# Classe Aluno e Classe Escola
# Aluno: atributos nome, idade, curso. Método apresentar().
# Escola: atributos nome, lista_de_alunos.
# Método adicionar_aluno(aluno).
# Método listar_alunos().
# Desafio: criar 2 alunos e adicioná-los na escola, exibindo a lista.


class Aluno:
    def __init__(self, nome: str, idade: int, curso: str):
        self.nome = nome
        self.idade = idade
        self.curso = curso

    def __str__(self):
        return (
            "-- Aluno --\n"
            f"Nome: {self.nome}\n"
            f"Idade: {self.idade}\n"
            f"Curso: {self.curso}\n"
        )


class Escola:
    def __init__(self, nome: str, alunos: list[Aluno] = []):
        self.nome = nome
        self.alunos = alunos

    def __len__(self):
        return len(self.alunos)

    def __str__(self):
        return "-- Escola --\n" f"Nome: {self.nome}\n" f"Qtd Alunos: {len(self)}\n"

    def adicionar_aluno(self, aluno: Aluno) -> None:
        self.alunos.append(aluno)

    def listar_alunos(self) -> None:
        print(self)
        if self.alunos:
            print("Alunos: ")
            for aluno in self.alunos:
                print(aluno)

    def listar_alunos_por_curso(self, curso: str):
        encontrou = False
        if self.alunos:
            for aluno in self.alunos:
                if aluno.curso.lower() == curso.lower():
                    print(aluno)
                    encontrou = True
        if not encontrou:
            print("Não há alunos do curso informado")

    def listar_alunos_por_nome(self, pesquisa: str):
        encontrou = False
        if self.alunos:
            for aluno in self.alunos:
                if pesquisa.lower() in aluno.nome.lower():
                    print(aluno)
                    encontrou = True
        if not encontrou:
            print("Não há alunos com nome informado na pesquisa")


if __name__ == "__main__":
    escola = Escola("Baixinhos não educados")

    aluno1 = Aluno("Gabriel Pereira", 13, "1º E. M.")
    aluno2 = Aluno("Fulano da Silva", 14, "2º E. M.")
    aluno3 = Aluno("Beltrano Marques", 14, "2º E. M.")
    aluno4 = Aluno("Siclano Oliveira da Silva", 15, "3º E. M.")

    escola.adicionar_aluno(aluno1)
    escola.adicionar_aluno(aluno2)
    escola.adicionar_aluno(aluno3)
    escola.adicionar_aluno(aluno4)


    print("\n-- Listando todos os alunos --")
    escola.listar_alunos()

    print("\n-- Listando alunos por curso --")
    escola.listar_alunos_por_curso("2º E. M.")
    print("\n-- Listando alunos por pesquisa do nome --")
    escola.listar_alunos_por_nome("Da Silva")

