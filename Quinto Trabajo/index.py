
opcion = 0

while opcion != 3:
    print("\nMenú Principal")
    print("1. ")
    print("2. Serie de taylor")
    print("3. Salir")

    try:
        opcion = int(input("Ingresa una opción: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue  

    if opcion == 1:
        print("Hola amor")

    elif opcion == 2:
        print("Serie de Taylor")
    elif opcion == 3:
        print("Adios")
    else:
        print("Error: Ingresa una opción válida.")
        continue
    