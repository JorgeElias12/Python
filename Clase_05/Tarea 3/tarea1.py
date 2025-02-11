#Número aleatorio y doble
#Crea una función que genere un número aleatorio entre 1 y 10 y retorne su doble.
import random

def doble_aleatorio():
    return random.randint(1, 10) * 2

print(doble_aleatorio())