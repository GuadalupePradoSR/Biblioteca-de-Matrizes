#FINALIZADA item 4
def diagonal_principal_secundaria_maior_elemento_posicao():
    from random import random
    la = int(input("Digite a quantidade de linhas da Matriz A: "))
    ca = int(input("Digite a quantidade de colunas da Matriz A: "))
    A = [None] * la
    print()
    
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

    if la == ca:
        #imprimir diagonal principal
        print("Diagonal principal:")
        for i in range(la):
            print(A[i][i], end=" ")
        print()

        #imprimir diagonal secundária
        print("Diagonal secundária:")
        for i in range(la):
            print(A[i][la - i - 1], end=" ")
        print()
    else:
        maior = A[0][0]
        maior_posicao = (0, 0)

        for i in range(la):
            for j in range(ca):
                if A[i][j] > maior:
                    maior = A[i][j]
                    maior_posicao = (i, j)

        print(f"Maior elemento: {maior}")
        print(f"Posição do maior elemento: {maior_posicao}")
diagonal_principal_secundaria_maior_elemento_posicao()