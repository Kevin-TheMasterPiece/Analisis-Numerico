import math
import num2words

def numerosRomanos(numero):
    romanos = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL', 50: 'L', 
               90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
    resultado = ''
    for valor in sorted(romanos.keys(), reverse=True):
        while numero >= valor:
            resultado += romanos[valor]
            numero -= valor
    return resultado

class Cuadratica:
    @staticmethod
    def solucionar(a, b, c):
        tipo_S = b**2 - 4*a*c
        if tipo_S > 0:
            x1 = (-b + math.sqrt(tipo_S)) / (2*a)
            x2 = (-b - math.sqrt(tipo_S)) / (2*a)
            print(f"Las soluciones son x1 = {x1} y x2 = {x2}")
        elif tipo_S == 0:
            x = -b / (2*a)
            print(f"La solución única es x = {x}")
        else:
            x_r = -b / (2*a)
            x_i = math.sqrt(abs(tipo_S)) / (2*a)
            print(f"Las soluciones son complejas: x1 = {x_r} + {x_i}j y x2 = {x_r} - {x_i}j")

opcion = 0

while opcion != 4:
    print("\nMenú Principal")
    print("1. Convertir número a letras")
    print("2. Convertir número a romano")
    print("3. Calcular la cuadrática")
    print("4. Salir")

    try:
        opcion = int(input("Ingresa una opción: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue  

    if opcion == 1:
        try:
            numero = int(input("Ingresa el número: "))
            numero_letras = num2words.num2words(numero, lang='es')
            print(f"El número {numero} en letras es: {numero_letras}")
        except ValueError:
            print("El valor ingresado no es un número válido.")

    elif opcion == 2:
        try:
            numero = int(input("Ingresa el número: "))
            if numero <= 0 or numero >= 4000:
                print("Solo se aceptan números entre 1 y 3999.")
            else:
                print(f"El número {numero} en romano es: {numerosRomanos(numero)}")
        except ValueError:
            print("Error: Ingresa un número válido.")

    elif opcion == 3:
        try:
            a = float(input("Ingrese a: "))  
            b = float(input("Ingrese b: "))
            c = float(input("Ingrese c: "))
            if a == 0:
                print("El coeficiente 'a' no puede ser cero en una ecuación cuadrática.")
            else: 
                Cuadratica.solucionar(a, b, c)
        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")

    elif opcion == 4:
        print("Saliendo del programa...")

    else:
        print("Opción inválida. Inténtalo de nuevo.")
