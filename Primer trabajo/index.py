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
    def hipo(base, altura):
        return math.sqrt(base**2 + altura**2)
    
    @staticmethod
    def perimetro(base, altura, hipo):
        return base + altura + hipo

class Rectangulo:
    @staticmethod
    def area(base, altura):
        return base * altura
    
    @staticmethod
    def perimetro(base, altura):
        return 2 * (base + altura)

def mostrar_redondeos(valor, nombre):
    print(f"\nValores con reducción de decimales para {nombre}:")
    for i in range(10, -1, -1):
        print(f"Con {i} decimales: {round(valor, i)}")

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
        option_figura = int(input("Ingresa una opcion: "))
        
        if option_figura == 1:
            radio = float(input("Ingresa el radio: "))
            area = Circulo.area(radio)
            mostrar_redondeos(radio, "Radio")
            mostrar_redondeos(area, "Área del círculo")
        elif option_figura == 2:
            radio = float(input("Ingresa el radio: "))
            perimetro = Circulo.perimetro(radio)
            mostrar_redondeos(radio, "Radio")
            mostrar_redondeos(perimetro, "Perímetro del círculo")
    
    elif option == 2:
        print("1. Calcular area")
        print("2. Calcular hipotenusa del triangulo")
        print("3. Calcular perimetro del triangulo")
        option_figura = int(input("Ingresa una opcion: "))
        
        if option_figura == 1:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            area = Triangulo.area(base, altura)
            mostrar_redondeos(base, "Base del triángulo")
            mostrar_redondeos(altura, "Altura del triángulo")
            mostrar_redondeos(area, "Área del triángulo")
        elif option_figura == 2:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            hipo = Triangulo.hipo(base, altura)
            mostrar_redondeos(base, "Base del triángulo")
            mostrar_redondeos(altura, "Altura del triángulo")
            mostrar_redondeos(hipo, "Hipotenusa del triángulo")
        elif option_figura == 3:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            hipo = Triangulo.hipo(base, altura)
            perimetro = Triangulo.perimetro(base, altura, hipo)
            mostrar_redondeos(base, "Base del triángulo")
            mostrar_redondeos(altura, "Altura del triángulo")
            mostrar_redondeos(hipo, "Hipotenusa del triángulo")
            mostrar_redondeos(perimetro, "Perímetro del triángulo")
    
    elif option == 3:
        print("1. Calcular area")
        print("2. Calcular perimetro")
        option_figura = int(input("Ingresa una opcion: "))
        
        if option_figura == 1:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            area = Rectangulo.area(base, altura)
            mostrar_redondeos(base, "Base del rectángulo")
            mostrar_redondeos(altura, "Altura del rectángulo")
            mostrar_redondeos(area, "Área del rectángulo")
        elif option_figura == 2:
            base = float(input("Ingresa la base: "))
            altura = float(input("Ingresa la altura: "))
            perimetro = Rectangulo.perimetro(base, altura)
            mostrar_redondeos(base, "Base del rectángulo")
            mostrar_redondeos(altura, "Altura del rectángulo")
            mostrar_redondeos(perimetro, "Perímetro del rectángulo")
    
    elif option == 4:
        print("Adios")