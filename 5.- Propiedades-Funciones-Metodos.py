import numpy as np
a = np.array([12, 1, 4, 2, 1, 0])

# Propiedades
tipo = a.dtype
print('tipo: ', tipo)

dimensiones = a.ndim
print('dimensiones: ', dimensiones)

filcol = a.shape
print('filcol: ', filcol)

cantidad = a.size
print('cantidad: ', cantidad)

# Funciones y Metodos

# Suma de elementos
suma = np.sum(a)
print('suma: ', suma)
suma1 = a.sum()
print('suma1: ', suma1)

# Producto de todos los elementos
producto = np.prod(a)
print('producto: ', producto)

# Promedio de todos los elementos
promedio = np.mean(a)
print('promedio: ', promedio)

# Minimo valor
minimo = np.min(a)
print('minimo: ', minimo)

# Maximo valor
maximo = np.max(a)
print('maximo: ', maximo)

# Posición del minimo valor
posmin = np.argmin(a)
print('posmin: ', posmin)

# Posición del maximo valor
posmax = np.argmax(a)
print('posmax: ', posmax)

# Elementos unicos y ordena de menor a mayor
unicos = np.unique(a)
print('unicos: ', unicos)

# Ordenar de menor a mayor
ordenar = np.sort(a)
print('ordenar: ', ordenar)

# Ordena de menor a mayor los indices
# a = np.array([12, 1, 4, 2, 1, 0])
#              [5 1 4 3 2 0]
posiciones = np.argsort(a)
print('posiciones: ', posiciones)

# Desviación estándar
desviacion = np.std(a)
print('desviacion: ', desviacion)

# Varianza
varianza = np.var(a)
print('varianza: ', varianza)

# Producto Punto
prodPunt = np.dot(a, a)
print('prodPunt: ', prodPunt)

# Raíz cuadrada
raiz = np.sqrt(a)
print('raiz: ', raiz)

# Valores absolutos
valabs = np.abs(a)
print('valabs: ', valabs)

# Copy
copia = np.copy(a)
print('copia: ', copia)
