import numpy as np
# Crear un programa que muestre en pantalla 
# los nombres de los estudiantes que aprueban la materia
# Para aprobar la materia se debe obtener un promedio mayor igual a 60 
nombres = np.array(["Juan", "Maria", "Pedro", "Sara"])
nota1 = np.array([70, 62, 80, 45])
nota2 = np.array([50, 52, 71, 70])
nota3 = np.array([0, 75, 72, 60])

promedios = (nota1 + nota2 + nota3)/3
print('promedios: ', promedios)

vBool= promedios >=60
print('vBool: ', vBool)

resultado = nombres[vBool]
print('resultado: ', resultado)