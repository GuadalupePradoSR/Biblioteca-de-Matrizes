#FINALIZADA item 7
def X_igual_Btransposta_vezes_doispontocinco():
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

    if (lb != cb and lb != 1 and cb != 1):

        #transposta de B
        D = []
        for j in range(cb):
            nova_linhaB = []
            for i in range(lb):
                nova_linhaB += [B[i][j]]
            D += [nova_linhaB]

        #imprimindo a transposta de B
        print("Transposta de B:")
        for i in range(len(D)):
            for j in range(len(D[0])):
                print(D[i][j], end=" ")
            print()
        print()

        #multiplicar a transposta de B por 2.5
        for i in range(len(D)):
            for j in range(len(D[0])):
                D[i][j] *= 2.5

        #imprimir a operação de X
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
                    
                    while k * k <= numero:
                        if numero % k == 0:
                            ehprimo = 0
                            break
                        k += 1
                    primo = ehprimo
                quantidade += primo

        print(f"Quantidade de números primos na matriz B: {quantidade}")
X_igual_Btransposta_vezes_doispontocinco()