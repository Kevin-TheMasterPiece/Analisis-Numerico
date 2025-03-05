class Cambio_Octal:
    @staticmethod
    def decimal_a_octal(numero):
     if numero == 0:
        return "0"
     octal = ""
     while numero > 0:
        residuo = numero % 8
        octal = str(residuo) + octal
        numero //= 8
     return octal
    

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
            if numero < 0:
                print("No se aceptan números negativos.")
                continue
            else:
                num_bin = []
                while numero > 0:
                    num_bin.append(numero % 2)
                    numero = numero // 2
                print(f"El número en binario es: {''.join(map(str, num_bin[::-1]))}")
        elif opcion == 2:
            numero = int(input("Ingresa el número: "))
            
            print("el numero: ",numero,"en octal es: ", Cambio_Octal.decimal_a_octal(numero))
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