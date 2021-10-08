#funciones

"""
Funciones:

def [nombre función]():
    algoritmo o ejecución

se llaman:

[nombreFuncion]()
"""

#ejemplos:

def sumar(num1, num2):
    return num1+num2

def imprimirSaludo(saludo = "Hola"):
    print(saludo)


#Estructura datos tupla

#es como una lista pero no es modificable

# [nombre] = ([datos],[datos],[datos])

tupla = (1,2,3,4,5)

#Listas y tuplas anidadas

lista1 = [1,2,3]
lista2 = [4,5,6]

lista3 = [lista1,lista2]

tupla1 = (1,2,3)
tupla2 = (4,5,6)

tupla3 = (tupla1,tupla2)

#diccionarios

diccionario = {'nombre':'daniel','edad':22,'casado':False,'cursos':['C#','JS','PY']}
print(diccionario['nombre']) #imprimirá daniel
print(diccionario['cursos'][3]) #imprimirá PY

#ingresar valores a un diccionario

productos = {}
codigo = 1
nombre = "jabon"
precio = 115.5
stock = True

productos[codigo]=nombre,precio,stock
print(productos)