#3. Reto 11
#Funcion para ingresar la matriz
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
#Funcion para la matriz traspuesta 
def matriz_transpuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_transpuesta = []
    for j in range(columnas):
        fila = []
        for i in range(filas):
            fila.append(matriz[i][j])
        matriz_transpuesta.append(fila)
    
    return matriz_transpuesta

# Ingreso de la matriz
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))
matriz = ingresar_matriz(filas, columnas)

# Imprimir la matriz ingresada
print("\nMatriz ingresada:")
for fila in matriz:
    print(fila)

# Obtener la matriz transpuesta
matriz_transpuesta = matriz_transpuesta(matriz)

# Imprimir la matriz transpuesta
print("\nMatriz transpuesta:")
for fila in matriz_transpuesta:
    print(fila)