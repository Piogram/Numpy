# Crear un algoritmo que calcule el promedio de cada estudiante: ​

#El pasado
estudiante = ["Axell", "Paulette", "Josue", "Jhoanna"]
nota1 = [9, 1, 10, 7]
nota2 = [10, 6, 8, 9]
promedio = []
for i in range(len(estudiante)):
    n1=nota1[i]
    n2=nota2[i]
    resultado= (n1 + n2) / 2
    promedio.append(resultado)
print('promedio: ', promedio)
    

# Ahora:
import numpy as np
estudiante = np.array(["Axell", "Paulette", "Josue", "Jhoanna"])
nota1 = np.array([9, 1, 10, 7])
nota2 = np.array([10, 6, 8, 9])

promedio = (nota1 + nota2) / 2
print('promedio: ', promedio)
