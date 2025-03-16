import sympy as sp
import matplotlib.pyplot as plt
import numpy as np
def serie_taylor(funcion, variable, x0, n):
    #Calcula la serie de Taylor de una función en un punto x0 hasta el término n.
    return sp.series(funcion, variable, x0, n).removeO()

def garficar_funcion_taylor(funcion, taylor, variable, x0, rango=(-5, 5)):
    funcion_np=sp.lambdify(variable, funcion, 'numpy')
    taylor_np=sp.lambdify(variable, taylor, 'numpy')

    x=np.linspace(rango[0], rango[1], 400)
    y_funcion=funcion_np(x)
    y_taylor=taylor_np(x)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y_funcion, label="Función original", color="blue")
    plt.plot(x, y_taylor, label="Serie de Taylor", color="red", linestyle="--")
    plt.scatter([x0], [funcion_np(x0)], color="green", label=f"Punto x0 = {x0}", zorder=5)
    plt.axvline(x=x0, color="gray", linestyle=":", label=f"x = {x0}")  # Línea vertical en x0
    plt.title("Función original vs Serie de Taylor")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()

opcion = 0
while opcion != 3:
    print("\nMenú Principal")
    print("1. Newton-Raphson")
    print("2. Serie de taylor")
    print("3. Salir")

    try:
        opcion = int(input("Ingresa una opción: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue  

    if opcion == 1:
        print("Hola amor")

    elif opcion == 2:
        try:
            # Solicitar la función al usuario
            funcion_input = input("Ingrese la función con x como la variable (por ejemplo, 'sin(x)', 'exp(x)', 'log(x)', 'x**2 + 3*x + 1'): ")
            
            # Convertir la entrada en una expresión simbólica
            x = sp.symbols('x')
            funcion = sp.sympify(funcion_input)
            
            # Solicitar el punto x0 y el número de términos
            x0 = float(input("Ingrese el punto x0: "))
            n = int(input("Ingrese el número de términos de la serie: "))
             
            # Calcular la serie de Taylor
            taylor = serie_taylor(funcion, x, x0, n)
            
            # Mostrar el resultado
            print("La serie de Taylor de la función en el punto x0 es:", taylor)
            garficar_funcion_taylor(funcion, taylor, x, x0)
        
        except sp.SympifyError:
            print("Error: La función ingresada no es válida. Asegúrate de usar la sintaxis correcta (por ejemplo, 'x**2' para x al cuadrado).")
        except ValueError:
            print("Error: Ingresa un número válido.")
    elif opcion == 3:
        print("Adios")
    else:
        print("Error: Ingresa una opción válida.")
        continue
    