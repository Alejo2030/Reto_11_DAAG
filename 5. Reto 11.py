#5. Reto 11 
def sumar_fila(matriz, fila):
    suma = 0
    for valor in matriz[fila]:
        suma += valor
    return suma

# Pedir al usuario que ingrese la matriz
matriz = []
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la: "))
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor de la posición ({i}, {j}): "))
        fila.append(valor)
    matriz.append(fila)

print(matriz)

# Pedir al usuario que ingrese la fila que desea sumar
fila = int(input("Ingrese el número de fila que desea sumar: ")) # recordar que la primera columna seria cero porque en python se comienza a contar desde 0 

# Sumar la fila indicada
suma = sumar_fila(matriz, fila)
print("La suma de la fila " + str(fila) + " es :" + str(suma))