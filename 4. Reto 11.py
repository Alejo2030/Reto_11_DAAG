#4. Reto 11
def sumar_columna(matriz, columna):
    suma = 0
    for fila in matriz:
        suma += fila[columna]
    return suma

# Pedir al usuario que ingrese la matriz
matriz = []
filas = int(input("Ingrese el número de filas de la matriz: "))
columnas = int(input("Ingrese el número de columnas de la matriz: "))
for i in range(filas):
    fila = []
    for j in range(columnas):
        valor = int(input(f"Ingrese el valor de la posición ({i}, {j}): "))
        fila.append(valor)
    matriz.append(fila)


print (matriz) #Imprimir la matriz ingresada 
# Pedir al usuario que ingrese la columna que desea sumar
columna = int(input("Ingrese el número de columna que desea sumar: ")) # recordar que la primera columna seria cero porque en python se comienza a contar desde 0 

# Sumar la columna indicada
suma = sumar_columna(matriz, columna)
print("la suma de la columna " + str(columna) + " es: " + str(suma))
#Si se pone solo uancolumna la suma de esta sera el mismo valor que se pnga en la matriz ya que no se sumaria con nada 