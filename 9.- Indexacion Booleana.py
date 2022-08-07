import numpy as np

a = np.array([12, 1, 4, 7])
print('a: ', a)

# Cuales son los mayores a 2
vBool = a>2
print('vBool: ', vBool)
resultado = a[vBool]
print('resultado: ', resultado)

#Los Pares
vBool2= a%2 == 0
resultado2 = a[vBool2]
print('resultado2: ', resultado2)

#Los menores a 6
vBool3 = a<6
resultado3= a[vBool3]
print('resultado3: ', resultado3)


