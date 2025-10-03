class Paciente:
    def __init__(self, nome: str, idade: int, cpf: str, doenca: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.doenca = doenca

    def exibir_dados(self) -> None:
        print(
            f"""
        -- Dados do Paciente --
        Nome: {self.nome}
        Idade: {self.idade}
        CPF: {self.cpf}
        Doença: {self.doenca}
        """
        )

    def atualizar_doenca(self, nova_doenca: str) -> None:
        self.doenca = nova_doenca


paciente1 = Paciente("Gabriel", 27, "012.456.762-00", "Febre")
paciente2 = Paciente("Fulano", 21, "010.458.192-00", "Malária")

paciente1.exibir_dados()
paciente2.exibir_dados()

paciente1.atualizar_doenca("Virose")

paciente1.exibir_dados()
