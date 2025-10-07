# Atividade 02

# Um sistema de transporte precisa controlar os passageiros que entram em um ônibus.
# Cada passageiro tem nome e idade. O ônibus possui uma linha específica e uma capacidade máxima de passageiros.
# Implemente as classes necessárias para gerenciar os embarques e listar os passageiros dentro do ônibus.
# Se a capacidade for excedida, o sistema deve exibir uma mensagem de erro.Classe Passageiro e Classe Ônibus

# Passageiro: atributos nome, idade.
# Ônibus: atributos linha, capacidade, lista_passageiros.
# Método embarcar(passageiro).
# Método listar_passageiros().
# Desafio: criar um ônibus com capacidade 2 e tentar embarcar 3 passageiros (mostrar mensagem de erro ao tentar exceder).


class Passageiro:
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "-- Passageiro --\n" f"Nome: {self.nome}\n" f"Idade: {self.idade}\n"


class Onibus:
    def __init__(
        self, linha: str, capacidade: int = 3, passageiros: list[Passageiro] = []
    ):
        self.linha = linha
        self.capacidade = capacidade
        self.passageiros = passageiros

    def embarcar(self, passageiro: Passageiro):
        if len(self.passageiros) < self.capacidade:
            self.passageiros.append(passageiro)
            return
        print(
            "Não foi possível embacar o passageiro, o ônibus já atigiu a capacidade máxima!"
        )

    def listar_passageiros(self):
        for passageiro in self.passageiros:
            print(passageiro)

    def atualizar_capacidade(self, capacidade: int):
        if capacidade <= len(self.passageiros):
            print(
                "Capacidade inválida, precisa ser um número maior que a quantidade de passageiros atuais"
            )
            return
        self.capacidade = capacidade

    def obter_qtd_passageiros(self) -> int:
        return len(self.passageiros)


onibus = Onibus("101")

passageiro1 = Passageiro("Gabriel", 27)
passageiro2 = Passageiro("Pereira", 19)
passageiro3 = Passageiro("Fulano", 22)
passageiro4 = Passageiro("Siclano", 45)
passageiro5 = Passageiro("Beltrano", 34)

onibus.embarcar(passageiro1)
onibus.embarcar(passageiro2)
onibus.embarcar(passageiro3)
onibus.embarcar(passageiro4)

onibus.atualizar_capacidade(3)
print(onibus.obter_qtd_passageiros())
onibus.atualizar_capacidade(5)

onibus.embarcar(passageiro4)
onibus.embarcar(passageiro5)

onibus.listar_passageiros()
