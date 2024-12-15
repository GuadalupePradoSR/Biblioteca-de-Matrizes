from random import random

# Função para imprimir a matriz
def print_matriz(matriz):
    for row in matriz:
        for element in row:
            print(round(element, 2), end=" ")
        print()

# Função para realizar a eliminação de Gauss na matriz
def gauss_elimination(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    # Fase de eliminação
    for i in range(linhas):
        # Encontre o pivô (elemento na diagonal principal)
        pivot = matriz[i][i]

        # Normalize a linha atual dividindo pelo pivô
        for j in range(i, colunas):
            matriz[i][j] /= pivot

        # Subtrair a linha atual das linhas abaixo para zerar os elementos abaixo do pivô
        for k in range(i + 1, linhas):
            factor = matriz[k][i]
            for j in range(i, colunas):
                matriz[k][j] -= factor * matriz[i][j]

# Entrada do usuário
la = int(input("Digite a quantidade de linhas da Matriz A: "))
ca = int(input("Digite a quantidade de colunas da Matriz A: "))
A = []

# Preencher a matriz A com valores aleatórios
for i in range(la):
    linha = []
    for j in range(ca):
        linha.append(int(random() * 50))
    A.append(linha)

print("Matriz A:")
print_matriz(A)

# Executar a eliminação de Gauss na matriz A
gauss_elimination(A)

print("Matriz A após a eliminação de Gauss:")
print_matriz(A)
