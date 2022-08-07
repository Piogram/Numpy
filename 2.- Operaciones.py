import numpy as np
# El pasado:
lista1 = [1, 2, 3, 4, 5]
lista2 = [2, 4, 5, 6, 7]
resultado = []
for i in range(len(lista1)):
    e1 = lista1[i]
    e2 = lista2[i]
    resultado.append(e1+e2)

print('resultado: ', resultado)

# Ahora:
a = np.array([1, 2, 3, 4, 5])
b = np.array([2, 4, 5, 6, 7])
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a % b)
print(a**b)

# Broadcasting
c = np.array([1, 2, 3, 4, 5])
print(c+2)  # [1, 2, 3, 4, 5] + [2, 2, 2, 2, 2]
print(c-2)
