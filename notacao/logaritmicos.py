def busca_binaria(lista, alvo):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1

dados = [1, 3, 5, 7, 9, 11, 13, 15]

#print(busca_binaria(dados, 7))  # Retorna 3

# Exponenciacao 

def potencia_rapida(base, expoente):
    if expoente < 0:
        raise ValueError("O expoente deve ser um numero nao negativo")
    resultado = 1
    while expoente > 0:
        if expoente % 2 == 1:
            resultado *= base
        base *= base
        expoente //= 2
    return resultado
    
print(potencia_rapida(2, 10))

# Algoritmo de Euclides - Maximo divisor comum: 
def mdc(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
print(mdc(1000, 998))       