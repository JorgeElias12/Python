#Juego de adivinanza con intentos
#Modifica el ejercicio 4 para que el usuario tenga hasta 3 intentos para adivinar el número.

import random

num = random.randint(1, 10)
for _ in range(3):
    if int(input()) == num:
        print("Acertaste")
        break
else:
    print("Fallaste")