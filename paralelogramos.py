# Importo mis librerias correspondientes
import numpy as np
import matplotlib.pyplot as plt
#Mi funcion principal, para ingresar la funcion a integrar
def ingresar_funcion():
    funcion_str = input("Ingrese la función en formato Python (por ejemplo, 'x**2'): ")
    return lambda x: eval(funcion_str)
# Nota: Se debe respetar el formato, no se usa ^ para potencia
# Aquí pongo los límites de integración
def ingresar_limites(): 
    a = float(input("Ingrese el límite inferior de integración: "))
    b = float(input("Ingrese el límite superior de integración: "))
    return a, b
# Por último, el N° de paralelogramos, obviamente entre más mejor
def ingresar_numero_paralelogramos():
    n = int(input("Ingrese el número de paralelogramos para la aproximación: "))
    return n
# Aplico mu formula para la integral
def integral_por_paralelogramos(funcion, a, b, n):
    h = (b - a) / n
    x_values = np.linspace(a, b, n+1)
    y_values = funcion(x_values)
    integral_aproximada = h * np.sum(y_values[:-1] + y_values[1:]) / 2
    return integral_aproximada
# Funcion para graficar
def graficar_funcion_y_paralelogramos(funcion, a, b, n):
    x = np.linspace(a, b, 1000)
    y = funcion(x)
    x_paralelogramos = np.linspace(a, b, n+1)
    y_paralelogramos = funcion(x_paralelogramos)

    plt.plot(x, y, label='Función')
    plt.bar(x_paralelogramos, y_paralelogramos, width=(b-a)/n, alpha=0.5, label='Paralelogramos')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Aproximación de la integral por paralelogramos')
    plt.show()

# Vale, el usuario es libre de poner todos los valores y función
funcion = ingresar_funcion()
a, b = ingresar_limites()
n = ingresar_numero_paralelogramos()

# Calculo por ultimo y arrojo un resultado que me va a imprimir en la consola
resultado_aproximado = integral_por_paralelogramos(funcion, a, b, n)
print(f"Aproximación de la integral: {resultado_aproximado}")

graficar_funcion_y_paralelogramos(funcion, a, b, n)
