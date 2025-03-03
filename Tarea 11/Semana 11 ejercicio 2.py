# Definimos la nueva matriz 3x3 con los números solicitados y desordenados
matriz = [
    [18, 22, 21],
    [23, 19, 24],
    [25, 26, 20]
]

# Función para ordenar una fila específica de la matriz usando QuickSort
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def ordenar_fila(matriz, fila):
    matriz[fila] = quicksort(matriz[fila])

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Especificamos la fila a ordenar (en este caso, fila 2)
fila_a_ordenar = 2  # Cambiado a 2 para ordenar la fila 2
ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz después de ordenar la fila
print("\nMatriz después de ordenar la fila", fila_a_ordenar, ":")
for fila in matriz:
    print(fila)

