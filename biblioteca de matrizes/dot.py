#dot
def dot():
    from random import random
    la = int(input("Digite a quantidade de linhas da Matriz A: "))
    ca = int(input("Digite a quantidade de colunas da Matriz A: "))
    lb = int(input("Digite a quantidade de linhas da Matriz B: "))
    cb = int(input("Digite a quantidade de colunas da Matriz B: "))
    A = [None] * la
    B = [None] * lb
    print()

    if ca != lb:
        print("As matrizes não podem ser multiplicadas devido às dimensões incompatíveis.")
        return

    #matriz A linha
    for i in range(len(A)):
        A[i] = [None] * ca
    #matriz A coluna
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = int(random() * 50)

    #matriz B linha
    for i in range(len(B)):
        B[i] = [None] * cb
    #matriz B coluna
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = int(random() * 50)

    #imprimir com quebra de linha
    print("Matriz A:")
    for i in range(la):
        for j in range(ca):
            print(A[i][j], end=" ")
        print( )
    print()

    print("Matriz B:")
    for i in range(lb):
        for j in range(cb):
            print(B[i][j], end=" ")
        print( )
    print()

    #inicializar a matriz de resultado t com zeros
    t = [[0 for _ in range(cb)] for _ in range(la)]

    #multiplicação das matrizes A e B
    for i in range(la):
        for j in range(cb):
            for k in range(ca):
                t[i][j] += A[i][k] * B[k][j]

    #imprimindo o produto
    print("\nResultado da multiplicação de A por B:")
    for row in t:
        print(row)

dot()