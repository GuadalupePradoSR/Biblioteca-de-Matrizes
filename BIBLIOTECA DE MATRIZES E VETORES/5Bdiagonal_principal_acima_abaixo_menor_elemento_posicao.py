#FINALIZADO item 5
def diagonal_principal_acima_abaixo_menor_elemento_posicao():
    from random import random
    lb = int(input("Digite a quantidade de linhas da Matriz B: "))
    cb = int(input("Digite a quantidade de colunas da Matriz B: "))
    B = [None] * lb
    print()

    #matriz B linha
    for i in range(len(B)):
        B[i] = [None] * cb
    #matriz B coluna
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = int(random() * 50)

    #imprimir com quebra de linha
    print("Matriz B:")
    for i in range(lb):
        for j in range(cb):
            print(B[i][j], end=" ")
        print( )
    print()

    if lb == cb:
        #imprimir diagonal principal
        print("Diagonal principal:")
        for i in range(lb):
            print(B[i][i], end=" ")
        print()

        print("Elementos acima da diagonal principal:")
        for i in range(lb):
            for j in range(i + 1, cb):
                print(B[i][j], end=" ")
        print()

        print("Elementos abaixo da diagonal principal:")
        for i in range(1, lb):
            for j in range(i):
                print(B[i][j], end=" ")
        print()
    else:
        menor_elemento = B[0][0]
        menor_posicao = (0, 0)

        for i in range(lb):
            for j in range(cb):
                if B[i][j] < menor_elemento:
                    menor_elemento = B[i][j]
                    menor_posicao = (i, j)

        print(f"Menor elemento da Matriz B: {menor_elemento}")
        print(f"Posição do menor elemento: {menor_posicao}")
diagonal_principal_acima_abaixo_menor_elemento_posicao()
