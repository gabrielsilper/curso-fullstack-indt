class Livro:
    def __init__(self, nome: str, autor: str, qtd_paginas: int, edicao: int):
        self.nome = nome
        self.autor = autor
        self.qtd_paginas = qtd_paginas
        self.edicao = edicao

    def __str__(self):
        return (
            "-- Livro --\n"
            f"Nome: {self.nome}\n"
            f"Autor: {self.autor}\n"
            f"Paginas: {self.qtd_paginas}\n"
            f"Edição: {self.edicao}"
        )


class Biblioteca:
    def __init__(self, nome: str, livros: list[Livro] = []):
        self.nome = nome
        self.livros = livros

    def __str__(self):
        return "-- Biblioteca --\n" f"Nome: {self.nome}"

    def adicionar_livro(self, livro: Livro) -> None:
        self.livros.append(livro)

    def listar_livros(self) -> None:
        print(self)
        if not self.livros:
            print("Ainda não há livros disponíveis")
        print("Lista de livro disponíveis: ")
        for livro in self.livros:
            print(livro)


biblioteca = Biblioteca("Livrinhos")

livro1 = Livro("Livro 1", "Autor 1", 100, 1)
livro2 = Livro("Livro 2", "Autor 2", 200, 2)
livro3 = Livro("Livro 3", "Autor 3", 300, 3)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.adicionar_livro(livro3)

biblioteca.listar_livros()
