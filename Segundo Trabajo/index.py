def numerosRomanos(numero):
    romanos= {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    resultado = ''
    for valor in sorted(romanos.keys(), reverse=True):
     while numero >= valor:
        resultado += romanos[valor]
        numero -= valor
    return resultado
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
        if numero <= 0 or numero>4000:
            print("No se aceptan numeros negativos ni numeros mayores a 3999")
        else:
            print(numerosRomanos(numero))
    elif opcion == 3:
        print("Cuadratica")
    elif opcion == 4:
        print("Saliendo del programa")
    else:
        print("Opcion invalida")  
     