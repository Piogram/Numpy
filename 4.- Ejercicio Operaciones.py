# Calcular el IMC de los datos de peso  y altura  guardados en 2 listas/arreglos
# IMC = peso / (altura**2)

# El pasado
pesos = [72, 62, 80, 65]
alturas = [1.71, 1.62, 1.72, 1.59]
imc=[]
for i in range(len(pesos)):
    peso= pesos[i]
    altura = alturas[i]
    total= peso /(altura**2)
    imc.append(total)
print('imc: ', imc)

# Ahora:
import numpy as np
pesos = np.array([72, 62, 80, 65])
alturas = np.array([1.71, 1.62, 1.72, 1.59])
imc= pesos / (alturas**2)
print('imc: ', imc)

