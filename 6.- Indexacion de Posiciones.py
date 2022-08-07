import numpy as np

vector = np.array([6, 7, 8, 9, 10])
#                 [0, 1, 2, 3,  4]

posiciones = np.array([0,4,1,3])


resultado = vector[posiciones]
print('resultado: ', resultado)

