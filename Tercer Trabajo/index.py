opcion = 0

while opcion != 3:
    try:
        print("MENU PRINCIPAL")
        print("1. Calcular el error absoluto y relativo de una tabla de frecuendias")
        print("2. Calcular medidad de tendencia central para datos agrupados")
        print("3. Salir")
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:
            xi = [3.50, 3.60, 3.35, 4.10, 4.01, 4.40, 4.57]
            f = [1, 2, 3, 3, 3, 2, 1]
            fa = []
            n = sum(f)
            
            for i in range(len(f)):
                if i == 0:
                    fa.append(f[i])
                else:
                    ant = fa[i-1]
                    suma = ant + f[i]
                    fa.append(suma)

            
            print(fa)

          
            
        elif opcion == 2:
            print("Hola")
        elif opcion == 3:
            print("Saliendo del programa")
        else:
            print("Digite una opcion valida")
    except ValueError:
        print("Digite un valor valido")