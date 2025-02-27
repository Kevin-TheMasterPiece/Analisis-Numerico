import random

opcion = 0

while opcion != 3:
    try:
        print("MENU PRINCIPAL")
        print("1. Calcular el error absoluto y relativo de una tabla de frecuendias")
        print("2. Calcular medida de tendencia central para datos agrupados")
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
            # Genera datos agrupados 
            intervalos = [(i, i+9) for i in range(1, 100, 10)]
            frecuencias = [random.randint(1, 10) for _ in intervalos]

            def punto_medio(intervalo):
             return (intervalo[0] + intervalo[1]) / 2
            
            #Media
            suma_frecuencias=sum(frecuencias)
            suma_productos = sum(f * punto_medio(intervalos[i]) for i, f in enumerate(frecuencias))
            media = suma_productos / suma_frecuencias

            #Mediana
            frecuencia_acumulada = [sum(frecuencias[:i+1]) for i in range(len(frecuencias))]
            mediana_intervalo = next(i for i, fa in enumerate(frecuencia_acumulada) if fa >= suma_frecuencias / 2)
            L = intervalos[mediana_intervalo][0]
            F_ant = frecuencia_acumulada[mediana_intervalo - 1] if mediana_intervalo > 0 else 0
            frecuencia_mediana = frecuencias[mediana_intervalo]
            h = intervalos[mediana_intervalo][1] - intervalos[mediana_intervalo][0]
            mediana = L + ((suma_frecuencias / 2 - F_ant) / frecuencia_mediana) * h


            #Moda
            moda_intervalo = frecuencias.index(max(frecuencias))  # Esto ya es el índice correcto
            L_moda = intervalos[moda_intervalo][0]  # Usamos moda_intervalo directamente
            d1 = frecuencias[moda_intervalo] - (frecuencias[moda_intervalo - 1] if moda_intervalo > 0 else 0)
            d2 = frecuencias[moda_intervalo] - (frecuencias[moda_intervalo + 1] if moda_intervalo < len(frecuencias) - 1 else 0)
            moda = L_moda + (d1 / (d1 + d2)) * h

            print("Intervalos y frecuencias:")
            for i, f in zip(intervalos, frecuencias):
                print(f"{i}: {f}")
            print(f"Media: {media}")
            print(f"Mediana: {mediana}")
            print(f"Moda: {moda}")
        elif opcion == 3:
            print("Saliendo del programa")
        else:
            print("Digite una opcion valida")
    except ValueError:
        print("Digite un valor valido")