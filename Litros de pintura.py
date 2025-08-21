#Escribe un programa para calcular la cantidad de litros de pintura necesarios para pintar una superficie.
# El programa debe leer el área de la superficie a pintar en metros cuadrados y la cantidad de metros cuadrados que se pueden cubrir con un litro de pintura. Y mostrar la cantidad de litros de pintura que se deben comprar para cubrir esa superficie.
# Considera que sólo se pueden comprar litros completos de pintura.
# Entradas:
# El área a pintar (número flotante)
# La cantidad de metros cuadrados que se pueden cubrir con un litro de pintura (número flotante)
# Salida
# La cantidad de litros a pintar (número entero)

import math

area = float(input("Ingresa el área a pintar"))
cantidad = float (input("Ingresa la cantidad de m2 que se pueden cubrir con un litro de pintura"))

litros = math.ceil (area/cantidad)

print(f"Se necesitan {litros} litros de pintura")