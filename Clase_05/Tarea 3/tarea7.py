#Menú interactivo
#Escribe una función que muestre un menú con opciones y use while para seguir mostrando el menú hasta que el usuario elija salir.

def menu():
    while True:
        print("\nMenú:")
        print("1. Saludar")
        print("2. Despedirse")
        print("3. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("¡Hola!")
        elif opcion == "2":
            print("¡Adiós!")
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")