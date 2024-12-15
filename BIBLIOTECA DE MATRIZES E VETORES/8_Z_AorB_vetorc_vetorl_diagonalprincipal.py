#F item 8
from random import random

def matriz_a():
    la = int(input("Digite a quantidade de linhas da Matriz A: "))
    ca = int(input("Digite a quantidade de colunas da Matriz A: "))
    A = [None] * la
    print()

    # matriz A linha
    for i in range(len(A)):
        A[i] = [None] * ca
    # matriz A coluna
    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = int(random() * 50)

    # imprimir com quebra de linha
    print("Matriz A:")
    for i in range(la):
        for j in range(ca):
            print(A[i][j], end=" ")
        print()
    print()
    return A

def matriz_b():
    lb = int(input("Digite a quantidade de linhas da Matriz B: "))
    cb = int(input("Digite a quantidade de colunas da Matriz B: "))
    B = [None] * lb
    print()

    # matriz B linha
    for i in range(len(B)):
        B[i] = [None] * cb
    # matriz B coluna
    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = int(random() * 50)

    # imprimir com quebra de linha
    print("Matriz B:")
    for i in range(lb):
        for j in range(cb):
            print(B[i][j], end=" ")
        print()
    print()
    return B

def Z_AorB_vetorc_vetorl_diagonalprincipal(la, ca, lb, cb):
    while True:
        N = int(input("Digite 1 ou 0: "))
        if N == 1:
            print()
            A = matriz_a()
            Z = [A]

            '''zeros = []
            for i in range(la):
                linhazero = []
                for j in range(ca):
                    linhazero += [0]
                zeros += [linhazero]'''

            if la == 1 or ca == 1:
                


        elif N == 0:
            print()
            B = matriz_b()
            Z = [B]
        
            if lb == 1 or cb == 1:



        else:
            print()
            print("Digite apenas 1 ou 0:")
            print()


A = matriz_a()
B = matriz_b()
Z_AorB_vetorc_vetorl_diagonalprincipal(len(A), len(A[0]), len(B), len(B[0]))