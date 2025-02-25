import math
class cuadratica:
   
    @staticmethod
    def solucionar(a,b,c):
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
        print(f"Las soluciones son complejas: x1 = {x_r} + {x_i}i y x2 = {x_r} - {x_i}i")

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
        a = float(input("Ingrese a: "))  
        b = float(input("Ingrese b: "))
        c = float(input("Ingrese c: "))
        if a == 0:
          print("El coeficiente 'a' no puede ser cero en una ecuación cuadrática.")
        else: 
           cuadratica.solucionar(a, b, c)

    elif opcion == 4:
        print("Saliendo del programa")
    else:
        print("Opcion invalida")  
     