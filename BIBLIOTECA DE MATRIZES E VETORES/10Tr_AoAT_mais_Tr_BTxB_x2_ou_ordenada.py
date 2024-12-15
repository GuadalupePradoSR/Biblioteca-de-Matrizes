#FINALIZADA item 10
def Tr_AoAT_mais_Tr_BTxB_x2_ou_ordenada():
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

    if la == ca and lb == cb:
        #transposta de A
        C = []
        for j in range(ca):
            nova_linhaA = []
            for i in range(la):
                nova_linhaA += [A[i][j]]
            C += [nova_linhaA]

        #imprimindo a transposta de A
        print("transposta de A:")
        for i in range(len(C)):
            for j in range(len(C[0])):
                print(C[i][j], end=" ")
            print()
        print()

        p = []
        for i in range(ca):
            linhap = []
            for j in range(la):
                linhap += [A[i][j] * C[i][j]]
            p += [linhap]

        #produto ponto a ponto de A e transposta de A
        print("Produto ponto a ponto de A e transposta de A:")
        for i in range(la):
            for j in range(ca):
                print(p[i][j], end=" ")
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
        print("transposta de B:")
        for i in range(len(D)):
            for j in range(len(D[0])):
                print(D[i][j], end=" ")
            print()
        print()

        #multiplicando transposta de B por B
        t = []
        for i in range(cb):
            linha = []
            for j in range(cb):
                soma = 0
                for k in range(lb):
                    soma += D[i][k] * B[k][j]
                linha += [soma]
            t += [linha]

        #imprimindo o produto
        print("multiplicação da transposta de B por B:")
        for i in range(cb):
            for j in range(cb):
                print(t[i][j], end=" ")
            print()
        print()

        #operação Tr - soma dos elementos da diagonal da matriz p e t
        diagonalp_soma = 0
        for i in range(ca):
            diagonalp_soma += p[i][i]

        #operação Tr da matriz t * 2 
        diagonalt_soma = 0
        for i in range(ca):
            diagonalt_soma += t[i][i]
        
        print(f"Soma dos elementos da diagonal principal do produto ponto a ponto de A e transposta de A: {diagonalp_soma}")
        print()
        print(f"Soma dos elementos da diagonal principal da multiplicação da transposta de B por B: {diagonalt_soma}")
        print()

        multiplicação = 0
        multiplicação += diagonalt_soma * 2
        print(f"Soma dos elementos da diagonal principal da multiplicação da transposta de B por B vezes 2: {multiplicação}")
        print()

        #soma da diagonal matrizes p e t*2
        s = diagonalp_soma + multiplicação
        print(f"Soma da soma dos elementos das diagonais principais: {s}")
        print()

    else:
        #lista vazia para armazenar os elementos da matriz A
        elementos_A = []

        #percorrer a matriz A e adicionar todos os elementos à lista
        for i in range(la):
            for j in range(ca):
                elementos_A += [A[i][j]]

        # Ordenar a lista em ordem crescente
        for i in range(len(elementos_A)):
            for j in range(i + 1, len(elementos_A)):
                if elementos_A[i] > elementos_A[j]:
                    elementos_A[i], elementos_A[j] = elementos_A[j], elementos_A[i]

        # Imprimir os elementos em forma de matriz
        print("Matriz A em ordem crescente:")
        posicaoA = 0
        for i in range(la):
            for j in range(ca):
                print(elementos_A[posicaoA], end=" ")
                posicaoA += 1
            print()
        print()

        #lista vazia para armazenar os elementos da matriz B
        elementos_B = []

        #percorrer a matriz A e adicionar todos os elementos à lista
        for i in range(lb):
            for j in range(cb):
                elementos_B += [B[i][j]]

        # Ordenar a lista em ordem decrescente
        for i in range(len(elementos_B)):
            for j in range(i + 1, len(elementos_B)):
                if elementos_B[i] < elementos_B[j]:
                    elementos_B[i], elementos_B[j] = elementos_B[j], elementos_B[i]

        # Imprimir os elementos em forma de matriz
        print("Matriz B em ordem decrescente:")
        posicaoB = 0
        for i in range(lb):
            for j in range(cb):
                print(elementos_B[posicaoB], end=" ")
                posicaoB += 1
            print()
        print()

Tr_AoAT_mais_Tr_BTxB_x2_ou_ordenada()