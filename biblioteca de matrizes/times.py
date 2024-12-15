def times():
    from random import random
    la = int(input("Digite a quantidade de linhas da Matriz A: "))
    ca = int(input("Digite a quantidade de colunas da Matriz A: "))
    lb = int(input("Digite a quantidade de linhas da Matriz B: "))
    cb = int(input("Digite a quantidade de colunas da Matriz B: "))
    A = [None] * la
    B = [None] * lb
    print()

    #verificar se as dimensões de A e B são iguais
    if la != lb or ca != cb:
        print("\nAs dimensões de A e B não são compatíveis para multiplicação elemento a elemento.")
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

    #multiplicação elemento a elemento de A e B
    C = [[A[i][j] * B[i][j] for j in range(ca)] for i in range(la)]

    # Imprimir o resultado da multiplicação
    print("Resultado da multiplicação elemento a elemento:")
    for row in C:
        print(row)

times()
