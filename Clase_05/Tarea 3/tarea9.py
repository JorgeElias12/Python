#Tabla de multiplicar infinita
#Crea una función que pida un número y muestre su tabla de multiplicar usando while, hasta que el usuario escriba salir.
while True:
    n = input()
    if n == "salir":
        break
    for i in range(1, 11):
        print(int(n) * i)
