#Suma de dos números aleatorios
#Escribe una función que genere dos números aleatorios entre 1 y 100 y retorne su suma.

import random

print("El doble del número aleatorio es:", random.randint(1, 10) * 2)
print("El resultado del lanzamiento del dado es:", random.randint(1, 6))
print("La suma de dos números aleatorios es:", sum(random.randint(1, 100) for _ in range(2)))
