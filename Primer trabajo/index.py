import math

class Circulo:
    @staticmethod
    def area(radio):
        return math.pi * radio ** 2

    @staticmethod
    def perimetro(radio):
        return 2 * math.pi * radio
class Triangulo:
    @staticmethod
    def area(base, altura):
        return base * altura / 2
    @staticmethod
    def perimetro (base, altura):
        return math.sqrt(base**2 + altura**2) 
        
option = 0

while option != 4:
    print("\nMenu principal\n")
    print("1. Circulo")
    print("2. Triangulo")
    print("3. Rectangulo")
    print("4. Salir")
    option = int(input("Ingresa una opcion: "))
    option_figura = 0
    
    if option == 1:

        print("1. Calcular area")
        print("2. Calcular perimetro de la circunferencia")
        print("3. Salir al menu principal")
        option_figura = int(input("Ingresa una opcion: "))
        
        if option_figura == 1:
            radio = float(input("Ingresa el radio: "))
            area = Circulo.area(radio)
            print("El area del circulo es: ")
            for i in range(10, -1, -1):
                print(f"Con {i} decimales: {round(area, i)}")
        elif option_figura == 2:
            radio = float(input("Ingresa el radio: "))
            perimetro = Circulo.perimetro(radio)
            print("El perimetro de la circunferencia es: ")
            for i in range(10, -1, -1):
                print(f"Con {i} decimales: {round(perimetro, i)}")
        elif option_figura == 3:
            print("Regresando al menu principal")
        else:
            print("Opcion invalida")
        
    elif option == 2:
        print("Triangulo")
        print("1. Calcular area")
        print("2. Calcular perimetro del triangulo")
        print("3. Salir al menu principal")
        option_figura = int(input("Ingresa una opcion: "))
        if option_figura == 1:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            area = Triangulo.area(base, altura)
            print("El area del triangulo es: ")
            for i in range(10, -1, -1):
                print(f"Con {i} decimales: {round(area, i)}")
        elif option_figura == 2:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            perimetro = Triangulo.perimetro(base, altura)
            print("El perimetro del triangulo es: ")
            for i in range(10, -1, -1):
                print(f"Con {i} decimales: {round(perimetro, i)}")
        elif option_figura == 3:
            print("Regresando al menu principal")
        else:
            print("Opcion invalida")
    elif option == 3:
        print("Rectangulo")
    elif option == 4:
        print("Adios")
    else:
        print("Opcion invalida")
