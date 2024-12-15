#sum
def sum():
    while True:
        from random import random
        la = int(input("Digite a quantidade de linhas da Matriz A: "))
        ca = int(input("Digite a quantidade de colunas da Matriz A: "))
        lb = int(input("Digite a quantidade de linhas da Matriz B: "))
        cb = int(input("Digite a quantidade de colunas da Matriz B: "))
        A = [None] * la
        B = [None] * lb
        print()

        if la == lb and ca == cb:
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

            #inicializar a matriz resultante da soma
            soma = [None] * la
            for i in range(len(soma)):
                soma[i] = [None] * ca

            #somar as matrizes A e B e armazenar o resultado na soma
            for i in range(la):
                for j in range(ca):
                    soma[i][j] = A[i][j] + B[i][j]

            #imprimir a matriz resultante da soma
            print("Matriz Soma (A + B):")
            for i in range(la):
                for j in range(ca):
                    print(soma[i][j], end=" ")
                print()
            break
        else:
            print("As linhas e colunas de A devem ser iguais as linhas e colunas de B")
            print()
sum()