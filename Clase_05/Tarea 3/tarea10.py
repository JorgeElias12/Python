#Suma acumulativa
#Escribe una función que pida números al usuario y los sume. El proceso se repite hasta que el usuario ingrese 0.

suma = 0
while (n := int(input())):
    suma += n
print(suma)
