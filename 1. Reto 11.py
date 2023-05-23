#1. Reto 11
def ingresar_matriz():
    filas = int(input("Ingrese el número de filas de la matriz: "))
    columnas = int(input("Ingrese el número de columnas de la matriz: "))
    matriz = []
    
    print("Ingrese los elementos de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = int(input(f"Ingrese el elemento en la posición [{i}][{j}]: "))
            fila.append(elemento)
        matriz.append(fila)
    
    return matriz

def suma_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    
    # Verificar que las matrices tienen las mismas dimensiones
    if filas != len(matriz2) or columnas != len(matriz2[0]):
        return None
    
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            suma = matriz1[i][j] + matriz2[i][j]
            fila.append(suma)
        resultado.append(fila)
    
    return resultado

def resta_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    
    # Verificar que las matrices tienen las mismas dimensiones
    if filas != len(matriz2) or columnas != len(matriz2[0]):
        return None
    
    resultado = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            resta = matriz1[i][j] - matriz2[i][j]
            fila.append(resta)
        resultado.append(fila)
    
    return resultado

# Ingreso de las matrices
print("Ingrese la primera matriz:")
matriz1 = ingresar_matriz()

print("Ingrese la segunda matriz:")
matriz2 = ingresar_matriz()

# Imprimir las matrices ingresadas
print("\nMatriz 1:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2:")
for fila in matriz2:
    print(fila)

# Suma de matrices
resultado_suma = suma_matrices(matriz1, matriz2)
if resultado_suma is not None:
    print("\nSuma de matrices:")
    for fila in resultado_suma:
        print(fila)
else:
    print("No se pueden sumar las matrices debido a dimensiones incorrectas.")

# Resta de matrices
resultado_resta = resta_matrices(matriz1, matriz2)
if resultado_resta is not None:
    print("\nResta de matrices:")
    for fila in resultado_resta:
        print(fila)
else:
    print("No se pueden restar las matrices debido a dimensiones incorrectas.")
