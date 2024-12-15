import copy

class Matriz:
    def __init__(self, dados):
        self.linhas = len(dados)
        self.colunas = len(dados[0])
        self.dados = dados

    def __getitem__(self, indice):
        return self.dados[indice]

    def __str__(self):
        resultado = ""
        for linha in self.dados:
            resultado += " ".join(map(str, linha)) + "\n"
        return resultado

    def eliminacao_gaussiana(matriz):
        linhas, colunas = matriz.linhas, matriz.colunas

        for linha_pivo in range(linhas):
            for linha in range(linha_pivo + 1, linhas):
                fator = matriz[linha][linha_pivo] / matriz[linha_pivo][linha_pivo]

                for coluna in range(colunas):
                    matriz[linha][coluna] -= fator * matriz[linha_pivo][coluna]

    def substituicao_retroativa(matriz):
        linhas, colunas = matriz.linhas, matriz.colunas
        resultado = Matriz([[0] for _ in range(linhas)])

        for i in range(linhas - 1, -1, -1):
            soma = 0
            for j in range(i + 1, colunas - 1):
                soma += matriz[i][j] * resultado[j][0]
            resultado[i][0] = (matriz[i][colunas - 1] - soma) / matriz[i][i]

        return resultado

def dot(A, B):
    if len(A[0]) != len(B):
        print("As matrizes não podem ser multiplicadas devido às dimensões incompatíveis.")
        return

    t = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                t[i][j] += A[i][k] * B[k][j]

    print("\nResultado da multiplicação de A por B:")
    for row in t:
        print(row)

def gauss_elimination(matriz):
    linhas = len(matriz.dados)
    colunas = len(matriz.dados[0])

    for linha_pivo in range(linhas):
        # Encontre o elemento de pivô
        pivo = matriz.dados[linha_pivo][linha_pivo]

        # Faça o elemento de pivô igual a 1
        for j in range(colunas):
            matriz.dados[linha_pivo][j] /= pivo

        # Elimine os outros elementos na coluna
        for linha in range(linha_pivo + 1, linhas):
            fator = matriz.dados[linha][linha_pivo]

            for j in range(colunas):
                matriz.dados[linha][j] -= fator * matriz.dados[linha_pivo][j]

    return matriz

def print_variaveis(matriz):
    linhas = len(matriz.dados)
    colunas = len(matriz.dados[0])
    print("\nSolução do Sistema:")
    for i in range(linhas):
        print(f"X{i + 1} = {matriz[i][colunas - 1]:.2f}")


def soma_matrizes(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("As matrizes A e B devem ter o mesmo número de linhas e colunas para a soma.")
        return

    soma = []
    for i in range(len(A)):
        linha_soma = []
        for j in range(len(A[0])):
            linha_soma.append(A[i][j] + B[i][j])
        soma.append(linha_soma)

    print("Matriz Soma (A + B):")
    for i in range(len(soma)):
        for j in range(len(soma[0])):
            print(soma[i][j], end=" ")
        print()

def times(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        print("\nAs dimensões de A e B não são compatíveis para multiplicação elemento a elemento.")
        return

    C = []

    for i in range(len(A)):
        row = []
        for j in range(len(A[0])):
            row.append(A[i][j] * B[i][j])
        C.append(row)

    print("Resultado da multiplicação elemento a elemento:")
    for row in C:
        print(row)

def transpose(A):
    print("Matriz A:")
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(A[i][j], end=" ")
        print()
    print()

    C = []
    for j in range(len(A[0])):
        nova_linhaA = []
        for i in range(len(A)):
            nova_linhaA.append(A[i][j])
        C.append(nova_linhaA)

    print("C (transposta de A):")
    for i in range(len(C)):
        for j in range(len(C[0])):
            print(C[i][j], end=" ")
        print()
    print()

def main():
    la = int(input("Digite a quantidade de linhas da Matriz A: "))
    ca = int(input("Digite a quantidade de colunas da Matriz A: "))

    A = []

    print("Digite os elementos da Matriz A:")
    for i in range(la):
        row = []
        for j in range(ca):
            elemento = int(input(f"Digite o elemento da posição ({i + 1}, {j + 1}): "))
            row.append(elemento)
        A.append(row)

    lb = int(input("Digite a quantidade de linhas da Matriz B: "))
    cb = int(input("Digite a quantidade de colunas da Matriz B: "))

    B = []

    print("Digite os elementos da Matriz B:")
    for i in range(lb):
        row = []
        for j in range(cb):
            elemento = int(input(f"Digite o elemento da posição ({i + 1}, {j + 1}): "))
            row.append(elemento)
        B.append(row)

    print("Matriz A:")
    for i in range(la):
        for j in range(ca):
            print(A[i][j], end=" ")
        print()

    print("Matriz B:")
    for i in range(lb):
        for j in range(cb):
            print(B[i][j], end=" ")
        print()

    matriz_a = Matriz(A)
    matriz_b = Matriz(B)

    while True:
        try:
            operacao = int(input("Digite a função (1: Multiplicação, 2: Eliminação Gaussiana, 3: Soma, 4: Multiplicação Elemento a Elemento, 5: Transposta): "))
            print()
            if operacao == 1:
                dot(A, B)

            elif operacao == 2:
                # Crie uma cópia da matriz original para a eliminação gaussiana
                matriz_temp = copy.deepcopy(matriz_a)
                gauss_elimination(matriz_temp)
                print("Matriz A após eliminação gaussiana:")
                print(matriz_temp)
                print_variaveis(matriz_temp)

            elif operacao == 3:
                soma_matrizes(A, B)

            elif operacao == 4:
                times(A, B)

            elif operacao == 5:
                transpose(A)

        except EOFError:
            break

if __name__ == "__main__":
    main()
