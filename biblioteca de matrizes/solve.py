from random import random

class Matriz:
    # O método __init__ cria uma matriz de dimensões especificadas (linhas e colunas) preenchida com zeros.
	#self.linhas e self.colunas são atributos para armazenar o número de linhas e colunas da matriz.
    def init(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.dados = [[0 for _ in range(colunas)] for _ in range(linhas)]

	# O método getitem permite acessar elementos da matriz.
    def getitem(self, indice):
        return self.dados[indice]

	# O método str permite que a matriz seja representada como uma string quando for chamado.
    def str(self):
        resultado = ""
        for linha in self.dados:
            resultado += " ".join(map(str, linha)) + "\n"
        return resultado
    
# Esta função implementa o algoritmo de eliminação gaussiana para resolver sistemas de equações lineares representados por uma matriz aumentada.
# Percorre as linhas da matriz, encontra o fator de eliminação e atualiza a matriz.
def eliminacao_gaussiana(matriz):
    linhas, colunas = matriz.linhas, matriz.colunas

    for linha_pivo in range(linhas):
        for linha in range(linha_pivo + 1, linhas):
            fator = matriz[linha][linha_pivo] / matriz[linha_pivo][linha_pivo]

            for coluna in range(colunas):
                matriz[linha][coluna] -= fator * matriz[linha_pivo][coluna]

# Esta função implementa o processo de substituição retroativa para encontrar a solução de um sistema de equações lineares após a eliminação gaussiana.
# Percorre as linhas da matriz da última para a primeira, calculando os valores das variáveis desconhecidas.
def substituicao_retroativa(matriz):
    linhas, colunas = matriz.linhas, matriz.colunas
    resultado = Matriz(linhas, 1)

    for i in range(linhas - 1, -1, -1):
        soma = 0
        for j in range(i + 1, colunas - 1):
            soma += matriz[i][j] * resultado[j][0]
        resultado[i][0] = (matriz[i][colunas - 1] - soma) / matriz[i][i]

    return resultado

def resolver_sistema(aumentada):
    eliminacao_gaussiana(aumentada)
    return substituicao_retroativa(aumentada)

# Entradas
if __name__ == "__main__":
    linhas = int(input("Digite a quantidade de linhas da Matriz A: "))
    colunas = int(input("Digite a quantidade de colunas da Matriz A: "))

	# É criada uma instância da classe Matriz com as dimensões de acordo com as entradas, onde o número de colunas é aumentado em 1 para acomodar a coluna de resultados.
    matriz_aumentada = Matriz(linhas, colunas + 1)

	# Preenche a matriz com valores aleatórios.
    for i in range(linhas):
        for j in range(colunas):
            matriz_aumentada[i][j] = int(random() * 50)  # Preenche com números aleatórios

    for i in range(linhas):
        matriz_aumentada[i][colunas] = int(random() * 50)  # Preenche a coluna de resultados com números aleatórios

    print("Matriz Aumentada:")
    print(matriz_aumentada)

	# A função resolver_sistema é chamada para resolver o sistema de equações representado pela matriz aumentada.
    matriz_resultante = resolver_sistema(matriz_aumentada)
    
	# Imprimindo os valores das variáveis desconhecidas (X1, X2, etc.) com duas casas decimais. Esses valores são obtidos após a eliminação gaussiana e a substituição retroativa.
    print("\nSolução do Sistema:")
    for i in range(linhas):
        print(f"X{i+1} = {matriz_resultante[i][0]:.2f}")