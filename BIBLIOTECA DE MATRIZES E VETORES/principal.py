def principal():

    from random import random
    la = int(input("Digite a quantidade de linhas da Matriz A: "))
    ca = int(input("Digite a quantidade de colunas da Matriz A: "))
    lb = int(input("Digite a quantidade de linhas da Matriz B: "))
    cb = int(input("Digite a quantidade de colunas da Matriz B: "))
    A = [None] * la
    B = [None] * lb

    for i in range(len(A)):
        A[i] = [None] * ca

    for i in range(len(A)):
        for j in range(len(A[0])):
            A[i][j] = int(random() * 50)


    for i in range(len(B)):
        B[i] = [None] * cb

    for i in range(len(B)):
        for j in range(len(B[0])):
            B[i][j] = int(random() * 50)


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

#item 1
    def AxX_e_BxY(A, B, la, lb, ca, cb):
        X = int(input("Valor multiplicado pela Matriz A: "))
        Y = int(input("Valor multiplicado pela Matriz B: "))
        print()


        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] *= X


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

#item 2
    def C_transposta_A_e_D_transposta_B(A, B, la, lb, ca, cb):

        C = []
        for j in range(ca):
            nova_linhaA = []
            for i in range(la):
                nova_linhaA += [A[i][j]]
            C += [nova_linhaA]

        print("C (transposta de A):")
        for i in range(len(C)):
            for j in range(len(C[0])):
                print(C[i][j], end=" ")
            print()
        print()


        D = []
        for j in range(cb):
            nova_linhaB = []
            for i in range(lb):
                nova_linhaB += [B[i][j]]
            D += [nova_linhaB]

        print("D (transposta de B):")
        for i in range(len(D)):
            for j in range(len(D[0])):
                print(D[i][j], end=" ")
            print()

#item 3
    def A_mais_B(A, B, la, lb, ca, cb):
        while True:
            if la == lb and ca == cb:

                soma = [None] * la
                for i in range(len(soma)):
                    soma[i] = [None] * ca

                for i in range(la):
                    for j in range(ca):
                        soma[i][j] = A[i][j] + B[i][j]


                print("Matriz Soma (A + B):")
                for i in range(la):
                    for j in range(ca):
                        print(soma[i][j], end=" ")
                    print()
                break
            else:
                print("As linhas e colunas de A devem ser iguais as linhas e colunas de B")
                print()
    
#item 4
    def diagonal_principal_secundaria_maior_elemento_posicao(A, la, ca):
        if la == ca:

            print("Diagonal principal:")
            for i in range(la):
                print(A[i][i], end=" ")
            print()


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

#item 5
    def diagonal_principal_acima_abaixo_menor_elemento_posicao(B, lb, cb):
        if lb == cb:

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

#item 6
###

#item 7
    def X_igual_Btransposta_vezes_doispontocinco(B, lb, cb):
        if (lb != cb and lb != 1 and cb != 1):

            D = []
            for j in range(cb):
                nova_linhaB = []
                for i in range(lb):
                    nova_linhaB += [B[i][j]]
                D += [nova_linhaB]

            print("Transposta de B:")
            for i in range(len(D)):
                for j in range(len(D[0])):
                    print(D[i][j], end=" ")
                print()
            print()


            for i in range(len(D)):
                for j in range(len(D[0])):
                    D[i][j] *= 2.5

            print("Matriz X = transposta de B * 2.5:")
            for i in range(len(D)):
                for j in range(len(D[0])):
                    print(D[i][j], end=" ")
                print()
            print()
        else:

            quantidade = 0
            for i in range(lb):
                for j in range(cb):
                    numero = B[i][j]
                    primo = 1

                    if numero < 2:
                        primo = 0

                    else:
                        ehprimo = 1
                        k = 2
                        
                        while k <= numero:
                            if numero % k == 0:
                                ehprimo = 0
                                break
                            k += 1
                        primo = ehprimo
                    quantidade += primo

            print(f"Quantidade de números primos na matriz B: {quantidade}")

#item 8
###

#item 9
    def AxB_ProdutoMatricial(A, B, la, lb, ca, cb):
        Y = []
        print()

        if ca == lb:
            while True:

                for i in range(la):
                    linha = []
                    for j in range(cb):
                        elemento = 0
                        for k in range(ca):
                            elemento += A[i][k] * B[k][j]
                        linha += [elemento]
                    Y += [linha]

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

#item 10
    def Tr_AoAT_mais_Tr_BTxB_x2_ou_ordenada(A, B, la, lb, ca, cb):
        if la == ca and lb == cb:

            C = []
            for j in range(ca):
                nova_linhaA = []
                for i in range(la):
                    nova_linhaA += [A[i][j]]
                C += [nova_linhaA]

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

            print("Produto ponto a ponto de A e transposta de A:")
            for i in range(la):
                for j in range(ca):
                    print(p[i][j], end=" ")
                print()
            print()


            D = []
            for j in range(cb):
                nova_linhaB = []
                for i in range(lb):
                    nova_linhaB += [B[i][j]]
                D += [nova_linhaB]

            print("transposta de B:")
            for i in range(len(D)):
                for j in range(len(D[0])):
                    print(D[i][j], end=" ")
                print()
            print()


            t = []
            for i in range(cb):
                linha = []
                for j in range(cb):
                    soma = 0
                    for k in range(lb):
                        soma += D[i][k] * B[k][j]
                    linha += [soma]
                t += [linha]

            print("multiplicação da transposta de B por B:")
            for i in range(cb):
                for j in range(cb):
                    print(t[i][j], end=" ")
                print()
            print()


            diagonalp_soma = 0
            for i in range(ca):
                diagonalp_soma += p[i][i]


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


            s = diagonalp_soma + multiplicação
            print(f"Soma da soma dos elementos das diagonais principais: {s}")
            print()

        else:

            elementosA = []

            for i in range(la):
                for j in range(ca):
                    elementosA += [A[i][j]]


            for i in range(len(elementosA)):
                for j in range(i + 1, len(elementosA)):
                    if elementosA[i] > elementosA[j]:
                        elementosA[i], elementosA[j] = elementosA[j], elementosA[i]

            print("Matriz A em ordem crescente:")
            posicaoA = 0
            for i in range(la):
                for j in range(ca):
                    print(elementosA[posicaoA], end=" ")
                    posicaoA += 1
                print()
            print()


            elementosB = []

            for i in range(lb):
                for j in range(cb):
                    elementosB += [B[i][j]]


            for i in range(len(elementosB)):
                for j in range(i + 1, len(elementosB)):
                    if elementosB[i] < elementosB[j]:
                        elementosB[i], elementosB[j] = elementosB[j], elementosB[i]

            print("Matriz B em ordem decrescente:")
            posicaoB = 0
            for i in range(lb):
                for j in range(cb):
                    print(elementosB[posicaoB], end=" ")
                    posicaoB += 1
                print()
            print()


    while True:
        try:
            operacao = int(input("Digite a função: "))
            print()
            if operacao == 1:
                AxX_e_BxY(A, B, la, lb, ca, cb)

            elif operacao == 2:
                C_transposta_A_e_D_transposta_B(A, B, la, lb, ca, cb)

            elif operacao == 3:
                A_mais_B(A, B, la, lb, ca, cb)

            elif operacao == 4:
                diagonal_principal_secundaria_maior_elemento_posicao(A, la, ca)

            elif operacao == 5:
                diagonal_principal_acima_abaixo_menor_elemento_posicao(B, lb, cb)

            elif operacao == 6:
                pass

            elif operacao == 7:
                X_igual_Btransposta_vezes_doispontocinco(B, lb, cb)

            elif operacao == 8:
                pass

            elif operacao == 9:
                AxB_ProdutoMatricial(A, B, la, lb, ca, cb)

            elif operacao == 10:
                Tr_AoAT_mais_Tr_BTxB_x2_ou_ordenada(A, B, la, lb, ca, cb)
        
        except EOFError:
            break
principal()