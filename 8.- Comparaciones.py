import numpy as np

a = np.array([12, 1, 4, 7])
print('a: ', a)

b = np.array([10, 6, 4, 9])
print('b: ', b)

#Comparaciones
print("a>b: ", a>b)
print("a>=b: ", a>=b)
print("a<b: ", a<b)
print("a<=b: ", a<=b)
print("a==b: ", a==b)
print("a!=b: ", a!=b)
print("a > 2: ", a>2)
print("Pares:", a%2 == 0)
print(" (a<b) & (a>2) :",(a<b) & (a>2))
print(" (a<b) | (a>2) :",(a<b) | (a>2))
#any
resultado1= any(a>b)
print('resultado1: ', resultado1)

#all
resultado2= all(a>b)
print('resultado2: ', resultado2)