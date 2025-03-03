# Definimos la matriz 3x3 con números secuenciales comenzando desde 1
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Función para buscar un valor específico en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):  # Recorre las filas
        for j in range(len(matriz[i])):  # Recorre las columnas
            if matriz[i][j] == valor:
                return (i, j)  # Retorna la posición (fila, columna) si encuentra el valor
    return None  # Retorna None si no encuentra el valor

# Aquí puedes cambiar el valor a buscar
valor_a_buscar = 3 # Cambia este valor por el que desees buscar en la matriz

# Llamamos a la función para buscar el valor
posicion = buscar_valor(matriz, valor_a_buscar)

# Mostramos el resultado
if posicion:
    print(f"El valor {valor_a_buscar} se encontró en la posición {posicion}.")
else:
    print(f"El valor {valor_a_buscar} no se encontró en la matriz.")


