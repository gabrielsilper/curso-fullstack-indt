# Uma escola deseja classificar os alunos com base em suas notas;
# escreva um programa que receba do usuário o nome do aluno e 4
# notas, calcule a média e imprima o nome do aluno na primeira coluna
# e na segunda o texto reprovado caso a média seja menor que 5 e
# aprovado caso seja igual ou maior a 5.

QTD_NOTAS = 4
resultado_alunos = []

while True:
    aluno = input("Digite o nome do Aluno, digite 'Parar' para encerrar: ")

    if aluno.lower() == "Parar".lower():
        break

    soma_nota = 0
    for i in range(QTD_NOTAS):
        soma_nota += float(input(f"Digite a {i + 1}º nota: "))

    if soma_nota / QTD_NOTAS >= 5:
        resultado_alunos.append([aluno, "Aprovado"])
    else:
        resultado_alunos.append([aluno, "Reprovado"])

for resultado in resultado_alunos:
    print(resultado)
