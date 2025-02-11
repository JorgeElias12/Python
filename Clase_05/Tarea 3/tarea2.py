#Lanzamiento de un dado#Define una función que simule el 
#lanzamiento de un dado de 6 caras y devuelva el número obtenido.
import random

def lanzar_dado():
    return random.randint(1, 6)

print(lanzar_dado())