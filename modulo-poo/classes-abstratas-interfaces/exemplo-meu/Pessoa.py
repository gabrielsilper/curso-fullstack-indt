class Pessoa:
    def __init__(self, nome, idade, id=None):
        self.id = id
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return(f"Pessoa[id = {self.id}, nome = {self.nome}] idade = {self.idade}")
