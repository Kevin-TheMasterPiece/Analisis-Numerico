from tabulate import tabulate

opcion = 0

while opcion != 3:
    try:
        print("MENU PRINCIPAL")
        print("1. Calcular el error absoluto y relativo de una tabla de frecuendias")
        print("2. Calcular medidad de tendencia central para datos agrupados")
        print("3. Salir")
        opcion = int(input("Ingrese una opcion: "))

        if opcion == 1:

            xi = [3.50, 3.60, 3.35, 4.10, 4.01, 4.40, 4.57, 3.75, 3.85, 3.95, 4.20, 4.30, 4.50, 4.60, 4.70, 3.45, 3.55, 3.65, 3.75, 3.85, 3.95, 4.05, 4.15, 4.25, 4.35, 4.45, 4.55, 4.65, 4.75, 4.85]
            f = [1, 2, 3, 3, 3, 2, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
            fa = []
            n = sum(f)
            
            for i in range(len(f)):
                if i == 0:
                    fa.append(f[i])
                else:
                    ant = fa[i-1]
                    suma = ant + f[i]
                    fa.append(suma)

            xifi = [round(xi[i] * f[i], 4) for i in range(len(xi))]
            sumXiFi = round(sum(xifi), 4)
            
            x = round(sumXiFi / n, 4)
            
            eatabla = []

            for i in xi:
                elemento = round(abs(x-i), 4)
                eatabla.append(elemento)
            
            sumEaTabla = round(sum(eatabla), 4)
            ea = round(sumEaTabla / n, 4)
            er = round((ea / x) * 100, 4)

            headers = ["", "Xi", "f", "fa", "Xi . f", "Ea"]
            table = [[i+1, xi[i], f[i], fa[i], xifi[i], eatabla[i]] for i in range(len(xi))]
            table.append(["", "", "", "", "Sum:" + str(sumXiFi), "Sum:" + str(sumEaTabla)])
            

            # Imprimir la tabla
            print(tabulate(table, headers, tablefmt="grid"))

            print(f"Media aritmética: {x}")
            print(f"Error absoluto (Ea): {ea}")
            print(f"Error relativo (Er): {er}%")

             
        elif opcion == 2:
            print("Hola")
        elif opcion == 3:
            print("Saliendo del programa")
        else:
            print("Digite una opcion valida")
    except ValueError:
        print("Digite un valor valido")