#Lista de números aleatorios
#Define una función que genere una lista con 5 números aleatorios entre 1 y 50 y la retorne.
import random

print([random.randint(1, 50) for _ in range(5)])