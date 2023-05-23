#2. Reto 11
def ingresar_matriz(filas, columnas):
    matriz = []
    
    print("Ingrese los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento en la posición [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
    
    return matriz

def producto_matrices(matriz1, matriz2):
    filas_matriz1 = len(matriz1)
    columnas_matriz1 = len(matriz1[0])
    filas_matriz2 = len(matriz2)
    columnas_matriz2 = len(matriz2[0])
    
    # Verificar que el número de columnas de matriz1 es igual al número de filas de matriz2
    if columnas_matriz1 != filas_matriz2:
        return None
    
    resultado = []
    for i in range(filas_matriz1):
        fila = []
        for j in range(columnas_matriz2):
            producto = 0
            for k in range(columnas_matriz1):
                producto += matriz1[i][k] * matriz2[k][j]
            fila.append(producto)
        resultado.append(fila)
    
    return resultado

# Ingreso de las matrices
filas_matriz1 = int(input("Ingrese el número de filas de la primera matriz: "))
columnas_matriz1 = int(input("Ingrese el número de columnas de la primera matriz: "))
matriz1 = ingresar_matriz(filas_matriz1, columnas_matriz1)

filas_matriz2 = int(input("Ingrese el número de filas de la segunda matriz: "))
columnas_matriz2 = int(input("Ingrese el número de columnas de la segunda matriz: "))
matriz2 = ingresar_matriz(filas_matriz2, columnas_matriz2)

# Imprimir las matrices ingresadas
print("\nMatriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

# Producto de matrices
resultado_producto = producto_matrices(matriz1, matriz2)
if resultado_producto is not None:
    print("\nProducto de matrices:")
    for fila in resultado_producto:
        print(fila)
else:
    print("No se puede realizar el producto de matrices debido a dimensiones incorrectas.")