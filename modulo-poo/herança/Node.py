class Personagem:
    def __init__(self, nome: str, poder: int, tipo: str):
        self.nome = nome
        self.poder = poder
        self.tipo = tipo


class Chefe_Floresta(Personagem):
    def __init__(self, nome, poder, tipo, reino):
        super().__init__(nome, poder, tipo)
        self.reino = reino

class Node:
    def __init__(self, personagem: Personagem = None):
        self.personagem = personagem
        self.esquerda : Node = None
        self.direita : Node = None

    def __str__(self):
        return (
            "           -- Node --           \n"
            "       ---            ---       \n"
            "   --Esq--             --Dir--  \n"
            f"{self.esquerda}  {self.direita}\n"
        )

    def adicionar_personagem(self, personagem: Personagem):
        if not self.personagem:
            self.personagem = personagem
            return
        if personagem.poder > self.esquerda.personagem.poder and self.esquerda:
            self.esquerda.adicionar_personagem(personagem)
        elif personagem.poder < self.direita.personagem.poder and self.direita:
            self.direita.adicionar_personagem(personagem)
        elif personagem.poder > self.esquerda.personagem.poder and not self.esquerda:
            self.esquerda = Node(personagem)
        elif personagem.poder < self.direita.personagem.poder and not self.direita:
            self.direita = Node(personagem)

class Arvore:
    def __init__(self , raiz: Node = None):
        self.raiz = raiz

    def adicionar_personagem_arvore(self, personagem: Personagem):
        self.raiz.adicionar_personagem(personagem)

    

personagem1 = Personagem("Elfo", 35, "Mágico")
personagem2 = Personagem("Humano", 12, "Normal")
personagem3 = Personagem("Elfo 2", 45, "Mágico")
chefe1 = Chefe_Floresta("Rei Orc", 67, "Mágico", "Trevas")

arvore = Arvore()

arvore.adicionar_personagem_arvore(personagem1)
arvore.adicionar_personagem_arvore(personagem2)
arvore.adicionar_personagem_arvore(personagem3)
arvore.adicionar_personagem_arvore(chefe1)

print(arvore.raiz)
