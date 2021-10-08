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


#listas

lista = [1,2,3,4,5]
listastring = ["daniel","Tatiana",]
listamix = ["daniel",22,False]
# Para conocer el tamaño de la lista len([nombre de la lista]) 
# se puede usar en un print print(len(lista))

#acceder a un elemento con el index  [nombre de la Lista][número index]
#ejemplo:  lista[0] -> 1
# listastring[0] -> daniel

#Para agregar un elemento se utiliza append([valor a agregar])
#ejemplo
lista.append(6)

#Para insertar en x index
#lista.insert([index],[valor agregar])

#para eliminar un valor de la lista
#lista.remove(valor a eliminar)


#con los indices negativos lo que hacemos es mostrar de atras en adelante si colocamos -1 
#muestra el último valor y así sucesivamente.
