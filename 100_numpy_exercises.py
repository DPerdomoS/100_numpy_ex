import os
os.chdir("C:\\Users\\dario\\Desktop\\CURSO UDEMY")
main_path = os.getcwd()


# 1. Importamos la libreria
import numpy as np

# 2. Imprimir la versión de numpy y su configuración
print(np.__version__)
np.show_config()

# 3. Creamos un vector nulo de tamaño 10
Z = np.zeros(10)
print(Z)

# 4. 

# 5. Creamos un vector nulo de tamaño 10 pero el 5 valor lo cambiamos por 1
Z = np.zeros(10)
Z[4] = 1
print(Z)

# 6. Crear un vector con valores desde 10 a 49
Z = np.arange(10,50)
print(Z)

# 7. Invertir un vector
Z = np.arange(50)
Z = Z[::-1]
print(Z)

# 8. Crear una matriz 3x3 con valor de 0 a 8
Z = np.arange(9).reshape(3,3)
print(Z)

# 9. Encontrar los indices diferentes de cero en un array [1,2,0,0,4,0]
nz = np.nonzero([1,2,0,0,4,0])
print(nz)

# 10. Crear una matriz 3x3 identidad
Z = np.eye(3)
print(Z)

# 11. Crear 3 matrices 3x3 con valores aleatorios
Z = np.random.random((3,3,3))
print(Z)

# 12. Crear un array 10x10 con valores aleatorios y encuentra el minimo y maximo
Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)

# 13. Crear un vector aleatorio de tamaño 30 y encuentra la media
Z = np.random.random(30)
print(Z.mean())

# 14. Crear un array 2d con 1 en el borde y 0 dentro
Z = np.ones((10,10))
Z[1:-1,1:-1] = 0

# 15. Cual es el resultado de la siguiente expresión?
0 * np.nan          # Nan
np.nan == np.nan    #  False
np.inf > np.nan     # False
np.nan - np.nan     # Nan
0.3 == 3 * 0.1      # False

# 16. Crear una matriz de 5x5 con valores de 1,2,3,4 en la diagonal inferior
Z = np.diag(np.arange(4), k = -1)
print(Z)

Z = np.diag(np.arange(1, 6), k = 0)
Z

# 17. Crear una matriz 8x8 y llenala con un patron de checkboard
Z = np.zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

# 18. Considere un array con forma (6,7,8), cual es el index de (x,y,z)
print(np.unravel_index(100,(6,7,8)))

# 19. Crear una matriz 8x8 usando la función tile
Z = np.tile(np.array([[0,1],[1,0]]), (4,4))

# 20. Normalice una matriz aleatoria de 5x5
Z = np.random.random((5,5))
Z_min, Z_max = Z.min(), Z.max()
Z = (Z - Z_min)/(Z_max - Z_min)
Z

# 21. Crear un dtype que describe un color como 4 valores
color = np.dtype([("r", np.ubyte, 1),
                    ("g", np.ubyte, 1),
                    ("b", np.ubyte, 1),
                    ("a", np.ubyte, 1)])

# 22. Multiplique una matriz 5x3 por 3x2
a = np.ones((5,3))
b = np.ones((3,2))
Z = np.dot(a, b)
Z.shape

# 23. Dado un array 1D, negar todos los elementos entre 3 y 8
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
Z

# 24. Cual es el resultado del siguiente script?
# Author: Jake VanderPlas
print(sum(range(5),-1))
# from numpy import *
print(sum(range(5),-1))
# Lo anterior sucede porque sum() es diferente a np.sum()

# 25. Considere un vector Z, cual de las siguientes es valida? 

# Z**Z # No
2 << Z >> 2
Z <- Z
1j*Z
Z/1/1
# Z<Z>Z

# 26. Cual es el resultado de las siguientes expresiones?

np.array(0) // np.array(0) # "//" Dividir y luego sacar el piso
np.array(0) // np.array(0.)
np.array(0) / np.array(0) # "/" Dividir
np.array(0) / np.array(0.)

# 27. Como redondear una matriz flotante?
# Author: Charles R Harris
Z = np.random.uniform(-10,+10,10)
print (np.trunc(Z + np.copysign(0.5, Z)))

# 28. Extraer la parte intera de un array usando 5 metodos diferentes
Z = np.random.uniform(0,10,10)
print (Z - Z%1)
print (np.floor(Z))
print (np.ceil(Z)-1)
print (Z.astype(int))
print (np.trunc(Z))

# 29. Crear una matriz 5x5 con valores de 0 a 4
Z = np.zeros((5,5))
Z = Z + np.arange(5)
print(Z)

# 30. Considere una función que genere 10 enteros y uselos como construir un array
def generate():
    xx = []
    for x in range(10):
        xx.append(x)
    return xx
Z = np.fromiter(generate(),dtype=float,count=-1)
print(Z)
















