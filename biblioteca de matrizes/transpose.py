#transpose
def transpose():
    from random import random
    la = int(input("Digite a quantidade de linhas da Matriz A: "))
    ca = int(input("Digite a quantidade de colunas da Matriz A: "))
    A = [None] * la

    #matriz A linha
    for i in range(len(A)):
        A[i] = [None] * ca
    #matriz A coluna
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = int(random() * 50)

    #imprimir com quebra de linha
    print("Matriz A:")
    for i in range(la):
        for j in range(ca):
            print(A[i][j], end=" ")
        print( )
    print()

    #transposta de A
    C = []
    for j in range(ca):
        nova_linhaA = []
        for i in range(la):
            nova_linhaA += [A[i][j]]
        C += [nova_linhaA]

    #imprimindo a transposta de A
    print("C (transposta de A):")
    for i in range(len(C)):
        for j in range(len(C[0])):
            print(C[i][j], end=" ")
        print()
    print()

transpose()