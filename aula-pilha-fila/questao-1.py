from collections import deque

lista = []
deque_lista = deque()
QTD_LIVROS = 10

for i in range(QTD_LIVROS):
    livro = input("Informe o nome do livro: ")
    lista.append(livro)
    deque_lista.append(livro)

if lista:
    print("Realizando pop na lista me retorna: ", lista.pop())

if deque_lista:
    print("Realizando pop na estrutura deque me retorna: ", deque_lista.pop())

if lista:
    print("O topo da lista me retorna: ", lista[-1])

if deque_lista:
    print("O topo da estrutura deque me retorna: ", deque_lista[-1])
