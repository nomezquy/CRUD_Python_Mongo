#clases y objetos

# self se utiliza para diferenciar los nombres internos a la clase /objeto de los exteriores
# en la ejecución

class Persona:
    nombre =''
    edad = 0
    def caminar(self):
        print(f"{self.nombre} empezó a caminar")

# Metodo con constructor
class Carro:
    def __init__(self,marca,color):
        self.marca = marca
        self.color = color

    def encender(self):
        print(f"Has encendido tu carro {self.marca}")



persona1 = Persona()
carro1 = Carro("Chevrolet","negro")
carro1.encender()

#Herencia

class trabajador(Persona):
    def __init__(self) -> None:
        super().__init__()

#ToString
"""
def __str__(self):
    cadena = self[atri1]+"," + self.apellido
    return cadena
"""