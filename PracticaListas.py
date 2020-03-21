matriz = [[2, 2, 5, 6], [0, 3, 7, 4], [8, 8, 5, 2], [1, 5, 6, 1]]


# Función que muestra la matriz en forma ordenada.
def mostrarMatriz(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=' ')
        print()


mostrarMatriz(matriz)

# Seleccionar el subarray [8 8 5 2].
print(matriz[2])

# Poner la diagonal de la matriz en cero.
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if i == j:
            matriz[i][j] = 0

mostrarMatriz(matriz)

# Sumar todos los elementos del array.
suma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        suma += matriz[i][j]
print(suma)

# Setear los valores pares en 0 y los impares en 1.
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 0
        else:
            matriz[i][j] = 1

mostrarMatriz(matriz)
