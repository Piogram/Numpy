import numpy as np
a = np.array([12, 1, 4, 2, 1, 0])

# Suma de elementos
suma= np.sum(a)
print('suma: ', suma)
print(a.sum())

# Producto de todos los elementos
print(np.prod(a))
print(a.prod())

# Promedio de todos los elementos
print(np.mean(a))
print(a.mean())

# Desviación estándar
print(np.std(a))
print(a.std())

# Minimo valor
print(np.min(a))
print(a.min())

# Maximo valor
print(np.max(a))
print(a.max())

# Posición del maximo valor
print(np.argmax(a))
print(a.argmax())

# Posición del minimo valor
print(np.argmin(a))
print(a.argmin())

# Elementos unicos y ordena de menor a mayor
print(np.unique(a))

# Ordena de menor a mayor
print(np.sort(a))
# print(a.sort()) ojo

# Ordena de menor a mayor los indices
print(np.argsort(a))
print(a.argsort())

