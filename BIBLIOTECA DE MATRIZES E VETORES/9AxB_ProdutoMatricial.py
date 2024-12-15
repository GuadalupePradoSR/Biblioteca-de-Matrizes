#FINALIZADA item 9
def AxB_ProdutoMatricial():
    while True:
        from random import random
        la = int(input("Digite a quantidade de linhas da Matriz A: "))
        ca = int(input("Digite a quantidade de colunas da Matriz A: "))
        lb = int(input("Digite a quantidade de linhas da Matriz B: "))
        cb = int(input("Digite a quantidade de colunas da Matriz B: "))
        A = [None] * la
        B = [None] * lb
        Y = []
        print()

        if ca == lb:
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

            #produto matricial AxB
            for i in range(la):
                linha = []
                for j in range(cb):
                    elemento = 0
                    for k in range(ca):
                        elemento += A[i][k] * B[k][j]
                    linha += [elemento]
                Y += [linha]

            # imprimir matriz resultante Y
            print("Matriz Y:")
            for i in range(la):
                for j in range(cb):
                    print(Y[i][j], end=" ")
                print()
            print()

            break
        else:
            print("Ordens de matrizes não casam para produto matricial.")
            print()

AxB_ProdutoMatricial()