import numpy as np

# Numpy utiliza una estructura de datos para manejo de vectores y matrices
# denominada array o arreglo.

arr = np.array([])

# Es muy similar a las listas en python, con la diferencia que los elementos
# de un arreglo deben ser del mismo tipo

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
