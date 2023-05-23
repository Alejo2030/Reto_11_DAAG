# Reto_11_DAAG


## :checkered_flag: Ánimo, ya reto 11 y  ya casi es Junio para ir a la casita !!!!:checkered_flag:


##  :lock:Desarrollo del reto!!!:unlock:

### :triangular_flag_on_post: 1.Desarrolle un programa que permita realizar la suma/resta de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.
 
### :moyai: Código
```ruby
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

```


### :triangular_flag_on_post: 2.Desarrolle un programa que permita realizar el producto de matrices. El programa debe validar las condiciones necesarias para ejecutar la operación.


### :moyai: Código

```ruby
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

```



### :triangular_flag_on_post: 3.Desarrolle un programa que permita obtener la matriz transpuesta de una matriz ingresada. El programa debe validar las condiciones necesarias para ejecutar la operación.


### :moyai: Código


```ruby
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
```




### :triangular_flag_on_post: 4.Desarrollar un programa que sume los elementos de una columna dada de una matriz.
### :moyai: Código


```ruby
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
```

### :triangular_flag_on_post: 5.Desarrollar un programa que sume los elementos de una fila dada de una matriz.
###  :moyai: Código

```ruby
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

```

## :blue_heart::blue_heart::blue_heart:Vamos Manchester City, campeones de UCL !!!!:blue_heart::blue_heart::blue_heart:
