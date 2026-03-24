def merge_sort(arr):
    # Caso base, lista com 1 ou zero elementos ja esta ordenada
    if len(arr) <= 1:
        return arr
    
    # Divide a lista ao meio
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Intercala as duas metades ordenadas
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0

    # Combina elementos em ordem crescente
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Adiciona os elementos restantes:
    merged.extend(left[i:])
    merged.extend(right[:j])
    return merged

# Exemplo de uso
dados = [68, 78, 12, 10, 24]
print(merge_sort(dados))

# QuickSort - Ordenacao rapida

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    menores = [x for x in arr if x < pivot]
    iguais = [x for x in arr if x == pivot]
    maiores = [x for x in arr if x > pivot]
    return quick_sort(menores) + iguais + quick_sort(maiores)

dados = [10, 7, 8, 9, 1, 5]
print("Quick sort: ", quick_sort(dados))

# Heap Sort - Ordenacao por heap

def heapify(arr, n, i):
    maior = i
    esquerda = 2 * i + 1
    direita = 2 * i + 2

    # Verifica filho esquerdo
    if esquerda < n and arr[esquerda] > arr[maior]:
        maior = esquerda
    # Verifica filho direito
    if direita < n and arr[direita] > arr[maior]:
        maior = direita

    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(arr):
    n = len(arr)

    # Constroi o heap maximo
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extrai elementos do heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

dados = [12, 11, 13, 5, 6, 7]
heap_sort(dados)                                                                                

print("Heap sort: ", dados)

