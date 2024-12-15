#FINALIZADA item 1
def AxX_e_BxY():
    from random import random
    la = int(input("Digite a quantidade de linhas da Matriz A: "))
    ca = int(input("Digite a quantidade de colunas da Matriz A: "))
    lb = int(input("Digite a quantidade de linhas da Matriz B: "))
    cb = int(input("Digite a quantidade de colunas da Matriz B: "))
    A = [None] * la
    B = [None] * lb
    X = int(input("Valor multiplicado pela Matriz A: "))
    Y = int(input("Valor multiplicado pela Matriz B: "))
    print()
    
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

    #multiplicar a matriz A por X
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] *= X

    #multiplicar a matriz B por Y
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] *= Y

    print(f"Matriz A multiplicada por {X}: ")
    for i in range(la):
        for j in range(ca):
            print(A[i][j], end=" ")
        print()
    print()

    print(f"Matriz B multiplicada por {Y}: ")
    for i in range(lb):
        for j in range(cb):
            print(B[i][j], end=" ")
        print()
AxX_e_BxY()