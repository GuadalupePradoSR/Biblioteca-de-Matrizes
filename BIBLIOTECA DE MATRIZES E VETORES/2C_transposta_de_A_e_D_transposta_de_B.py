#FINALIZADA item 2
def C_transposta_A_e_D_transposta_B():
    from random import random
    la = int(input("Digite a quantidade de linhas da Matriz A: "))
    ca = int(input("Digite a quantidade de colunas da Matriz A: "))
    lb = int(input("Digite a quantidade de linhas da Matriz B: "))
    cb = int(input("Digite a quantidade de colunas da Matriz B: "))
    A = [None] * la
    B = [None] * lb
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

    #transposta de B
    D = []
    for j in range(cb):
        nova_linhaB = []
        for i in range(lb):
            nova_linhaB += [B[i][j]]
        D += [nova_linhaB]

    #imprimindo a transposta de B
    print("D (transposta de B):")
    for i in range(len(D)):
        for j in range(len(D[0])):
            print(D[i][j], end=" ")
        print()
C_transposta_A_e_D_transposta_B()