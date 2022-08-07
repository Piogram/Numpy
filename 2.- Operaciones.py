# El pasado:
lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 4, 5, 6, 7]
resultado= []
for i in range(len(lista1)):
    e1 = lista1[i]
    e2 = lista2[i]
    total = e1 + e2
    resultado.append(total)
print('resultado: ', resultado)

# Ahora:
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 4, 5, 6, 7])

suma = a + b
print('suma: ', suma)

resta = a - b
print('resta: ', resta)

multiplicacion = a * b 
print('multiplicacion: ', multiplicacion)

division = a / b
print('division: ', division)

potencia = a ** b
print('potencia: ', potencia)

modulo = a % b
print('modulo: ', modulo)

# Broadcasting
c = np.array([1, 2, 3, 4, 5])

resultado1 = c + 2
print('resultado1: ', resultado1)

