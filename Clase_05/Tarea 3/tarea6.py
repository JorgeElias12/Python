#Contador regresivo
#Crea una función que reciba un número y haga una cuenta regresiva hasta 0 usando while.
def cuenta_regresiva(n):
    while n >= 0:
        print(n)
        n -= 1

cuenta_regresiva(50)