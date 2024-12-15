def linha_coluna_quebra(l,c):
    from random import random
    l = int(input("Digite a quantidade de linhas: "))
    c = int(input("Digite a quantidade de colunas: "))
    A = [None] * l
    B = [None] * l

    #matriz A linha
    for i in range(len(A)):
        A[i] = [None] * c
    #matriz A coluna
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = int(random() * 50)

    #matriz B linha
    for i in range(len(B)):
        B[i] = [None] * c
    #matriz B coluna
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = int(random() * 50)

    #imprimir com quebra de linha
    print("Matriz A:")
    for i in range(l):
        for j in range(c):
            print(A[i][j], end=" ")
        print( )
    print()

    print("Matriz B:")
    for i in range(l):
        for j in range(c):
            print(B[i][j], end=" ")
        print( )
    print()