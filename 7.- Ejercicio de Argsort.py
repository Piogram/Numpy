# Mostrar los nombres de los estudiantes ordenados de menor a mayor
# con respecto a su promedio.​

estudiante = ["Axell", "Paulette", "Josue", "Jhoanna"]
promedio = [9, 1, 10, 7]

# El pasado
resultado = [ ]
for i in range(len(promedio)):
    minimo = min(promedio)
    posminimo = promedio.index(minimo)
    est = estudiante[posminimo]
    resultado.append(est)
    estudiante.pop(posminimo)
    promedio.pop(posminimo)
print('resultado: ', resultado)



#Ahora
import numpy as np
estudiante = np.array(["Axell", "Paulette", "Josue", "Jhoanna"])
promedio = np.array([9, 1, 10, 7])

#Ahora
posiciones = np.argsort( promedio )
print('posiciones: ', posiciones)

resultado = estudiante[posiciones]
print('resultado: ', resultado)





























    
