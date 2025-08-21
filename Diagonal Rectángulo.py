#Escribe un programa que reciba el ancho y largo de un rectángulo y calcule la medida de la diagonal. Utiliza la función de la biblioteca math correspondiente.
# Entrada:
# Dos números flotantes, uno en cada renglón, correspondientes al ancho y largo del rectángulo.
# Salida:
# Un número, resultado del cálculo de la diagonal de dicho rectángulo

import math
ancho = float(input("Ingrese el ancho del rectangulo: "))
largo= float(input("Ingrese el largo del rectangulo: "))

hipotenusa = math.sqrt(math.pow(ancho, 2)) + math.pow(largo,2)

print("La diagonal del rectangulo mide", hipotenusa)