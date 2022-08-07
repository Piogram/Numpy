import numpy as np

# Numpy utiliza una estructura de datos para manejo de vectores y matrices
# denominada array o arreglo.

arr = np.array([1, 2, 3, 4, 5])

# Es muy similar a las listas en python, con la diferencia que los elementos
# de un arreglo deben ser del mismo tipo

#Index en Vectores
elemento = arr[0]
print('elemento: ', elemento)

#Slicing en Vectores
parte = arr[0:3]
print('parte: ', parte)

a = np.array(range(10), float)
print('a: ', a)

# Función arange(start=None, stop, step=None, dtype=None)
b = np.arange(10)
print('b: ', b)

c = np.arange(5, 10)
print('c: ', c)

d = np.arange(2, 10, 2)
print('d: ', d)

e = np.arange(10, dtype=float)
print('e: ', e)

#Función ones
f = np.ones(3)
print('f: ', f)

#Función zeros
g = np.zeros(7)
print('g: ', g)

g.fill(2)

print('g: ', g)