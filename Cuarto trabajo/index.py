def convertir_a_hexadecimal(numero):
    if numero < 0:
        return "No se puede convertir un número negativo."
    elif numero == 0:
        return 0
    else:
        hexadecimal = ""
        while numero > 0:
            residuo = numero % 16
            if residuo == 10:
                residuo = 'A'
            elif residuo == 11:
                residuo = 'B'
            elif residuo == 12:
                residuo = 'C'
            elif residuo == 13:
                residuo = 'D'
            elif residuo == 14:
                residuo = 'E'
            elif residuo == 15:
                residuo = 'F'
            numero = numero // 16
            hexadecimal = str(residuo) + hexadecimal
        return hexadecimal


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
            print(convertir_a_hexadecimal(numero))
        elif opcion == 4:
            print("Saliendo...")
        else:
            print("Opción no válida.")
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue