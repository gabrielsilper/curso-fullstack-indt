import numpy as np

QTD_ALUNOS = 4
QTD_DISCIPLINAS = 3

matriz = np.zeros((QTD_ALUNOS, QTD_DISCIPLINAS))

soma_notas_alunos = np.zeros(QTD_ALUNOS)
soma_notas_disciplinas = np.zeros(QTD_DISCIPLINAS)

for i in range(QTD_ALUNOS):
    for j in range(QTD_DISCIPLINAS):
        if j == 0:
            print("Disciplina - Matemática")
        elif j == 1:
            print("Disciplina - Português")
        else:
            print("Disciplina - Ciências")

        nota = float(input(f"Digite a nota do aluno {i + 1}: "))
        matriz[i][j] = nota
    print()

for i in range(QTD_ALUNOS):
    soma_nota_aluno = 0
    for j in range(QTD_DISCIPLINAS):
        soma_nota_aluno += matriz[i][j]
        soma_notas_disciplinas[j] += matriz[i][j]
    soma_notas_alunos[i] = soma_nota_aluno


for i in range(QTD_ALUNOS):
    print(
        f"A média do aluno {i + 1} nas disciplinas: ",
        soma_notas_alunos[i] / QTD_DISCIPLINAS,
    )

for j in range(QTD_DISCIPLINAS):
    if j == 0:
        print("Disciplina - Matemática")
    elif j == 1:
        print("Disciplina - Português")
    else:
        print("Disciplina - Ciências")
    print(f"A média da disciplina: ", soma_notas_disciplinas[i] / QTD_ALUNOS)
