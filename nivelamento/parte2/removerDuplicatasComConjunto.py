def remove_duplicatas(lista):
    if not isinstance(lista, list):
        raise TypeError("O parametro deve ser uma lista.")
    vistos = set()
    resultado = []

    for item in lista:
        if not isinstance(item, (int, float)):
            raise ValueError("Todos os elementos devem ser numeros")
        if item not in vistos:
            vistos.add(item)
            resultado.append(item)
    return resultado
numeros = []
while True:
    insert = input("Digite os numeros que deseja inserir na lista:")
    if insert == "":
        break
    try:
        numeros.append(int(insert))
    except ValueError:
        print("Entrada invalida. Por favor, digite um numero valido.")

print("Lista original:", numeros)
numeros_sem_duplicatas = remove_duplicatas(numeros)
print("Lista sem duplicatas:", numeros_sem_duplicatas)

