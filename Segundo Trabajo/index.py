

opcion = 0

while opcion != 4:
    print("\nMenu principal\n")
    print("1. Convertir numero a letras")
    print("2. Convertir numero a romano")
    print("3. Calcular la cuadratica")
    print("4. Salir")

    opcion = int(input("Ingresa una opcion: "))

    if opcion == 1:
        numero = int(input("Ingresa el numero: "))
    elif opcion == 2:
        numero = int(input("Ingresa el numero: "))
    elif opcion == 3:
        print("Cuadratica")
    elif opcion == 4:
        print("Saliendo del programa")
    else:
        print("Opcion invalida")  
     