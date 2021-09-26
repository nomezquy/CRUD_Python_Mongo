#Aspectos básicos de Python.

# comentario unica linea

"""
Esto es un comentario de varias lineas.
"""

#______________________________________________________________________________________

# Variable normal
variable = "daniel"
edad = 22
casado = False
altura = 185.5

# Variables Constantes

MI_VARIABLE = 1234
PI = 3.1416

#___________________________________________________________________________________

# Operadores Aritmeticos

# suma + Resta - multi * exponente ** division /  modulo %

#___________________________________________________________________________________
"""
Operadores de comparación

== Igual que

!= diferente que

> mayor que   >= mayor igual

< menor que   <= menor igual

"""
#___________________________________________________________________________________

# Operadores Lógicos

# and
# or
# not

#___________________________________________________________________________________

# impresiones e ingreso de datos en consola.

print("Esto es una impresión")
dato = input("Ingresando datos tipo string")
dato2 = int(input("Ingresando datos tipo int"))

# Concatenación

print("Daniel"+ " " + "Nomezquy")

#Interpolación

nombre = "Daniel"
anios = 22
print(f"{anios} son los años que tiene {nombre} ")