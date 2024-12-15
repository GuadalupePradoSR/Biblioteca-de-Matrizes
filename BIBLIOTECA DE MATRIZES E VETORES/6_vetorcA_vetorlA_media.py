#F item 6
def vetorcA_vetorlA_media():
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

    if la == 1:

        #vetor linha
        somaL = 0
        for j in range(ca):
            somaL += A[0][j]
        mediaL = somaL / ca

        print(f"Média dos valores do vetor linha: {mediaL}")

    elif ca == 1:

        #vetor coluna
        somaC = 0
        for i in range(la):
            somaC += A[i][0]
        mediaC = somaC / la

        print(f"Média dos valores do vetor coluna: {mediaC}")
        
    else:
        # Vetor de médias por linha
        Mlinhas = []
        for i in range(la):
            somaLinha = 0
            for j in range(ca):
                somaLinha += A[i][j]
            mediaLinha = somaLinha / ca
            Mlinhas += [mediaLinha]

        '''# Imprimir vetor de médias por linhas como matriz
        print("Vetor de médias por linhas (formato de matriz):")
        for i in range(la):
            print([Mlinhas[i]])'''

        print("Vetor de médias por linhas:")
        for i in range(la):
            print(f"Média da linha {i + 1}: {Mlinhas[i]}")

        # Vetor de médias por coluna
        Mcolunas = []
        for j in range(ca):
            somaColuna = 0
            for i in range(la):
                somaColuna += A[i][j]
            mediaColuna = somaColuna / la
            Mcolunas += [mediaColuna]

        '''# Imprimir vetor de médias por colunas como matriz
        print("Vetor de médias por colunas (formato de matriz):")
        for j in range(ca):
            print([Mcolunas[j]])
'''
        print("Vetor de médias por colunas:")
        for i in range(len(Mcolunas)):
           for j in range(ca):
            print(f"Média da coluna {j + 1}: {Mcolunas[j]}")

vetorcA_vetorlA_media()