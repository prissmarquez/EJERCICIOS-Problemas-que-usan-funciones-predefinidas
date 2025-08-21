"""
Desarrolla un programa en Python que calcule la distancia entre dos puntos del plano cartesiano.
Entradas:
El programa solicita el punto inicial (x1, y1) y el final (x2, y2). Todos enteros y en ese orden.

Salida:
El valor de la distancia (numero flotante) que existe entre los dos puntos. Despliega el resultado con la palabra distancia (todo en minúsculas) y un = y el número formateado a 2 decimales (sin espacios entre caracteres y números). Por ejemplo: distancia=9.90
"""
import math 

x1 = int(input("Ingresa el punto inicial x1: "))
y1 = int(input("Ingresa el punto inicial x1: "))
x2 = int(input("Ingresa el punto inicial x1: "))
y2 = int(input("Ingresa el punto inicial x1: "))

distancia = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print(f"Distancia = {distancia:.2f}")
