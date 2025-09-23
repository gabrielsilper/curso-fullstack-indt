import numpy as np

matriz1 = np.ones((3, 3))
matriz2 = np.zeros((2, 4))
matriz3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print(matriz3)
print("Primeira linha", matriz3[0, :])
print("Primeira coluna", matriz3[:, 2])
print("Submatriz", matriz3[1:3, 1:2])

matriz3[0, :] = 1
print(matriz3)

# np.sum soma todos os elementos da matriz
# np.sum [matriz,1] ele soma as linhas
# np.sum [matriz,0] ele soma as colunas
# np.dot faz multiplicação matricial