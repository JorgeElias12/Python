#Adivina el número (simple)
#Crea una función que genere un número aleatorio entre 1 y 10 y pida al usuario que adivine cuál es. Retorna si acertó o no.

import random

num = random.randint(1, 10)
print("¡adivina el numero!")
print("adivinaste" if int(input()) == num else "Fallaste")