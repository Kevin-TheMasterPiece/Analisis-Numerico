opcion = 0

while opcion != 4:
    print("\nMenú Principal")
    print("1. Convertir número a binario")
    print("2. Convertir número a octal")
    print("3. Convertir número a hexadecimal")
    print("4. Salir")

    try:
        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            numero = int(input("Ingresa el número: "))
            print(f"El número {numero} en binario es: {bin(numero)[2:]}")
        elif opcion == 2:
            numero = int(input("Ingresa el número: "))
            print(f"El número {numero} en octal es: {oct(numero)[2:]}")
        elif opcion == 3:
            numero = int(input("Ingresa el número: "))
            print(f"El número {numero} en hexadecimal es: {hex(numero)[2:]}")
        elif opcion == 4:
            print("Saliendo...")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue