def busca_linear(lista, alvo):
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1
dados = [10, 20, 30, 40, 50]
#print(busca_linear(dados, 30))  # Retorna 2

# Soma de elementos de uma lista

def soma_lista(lista):
    total = 0
    for num in lista:
        total += num
    return total
valores = [1, 2, 3, 4, 5]
print(soma_lista(valores))

def contar_ocorrencias(lista, alvo):
    contador = 0
    for item in lista:
        if item == alvo:
            contador += 1
    return contador

frutas = ['maca', 'maca', 'banana']
print(contar_ocorrencias(frutas, 'banana'))