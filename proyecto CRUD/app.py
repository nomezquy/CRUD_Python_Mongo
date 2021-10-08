import insert
import read
import update
import delete

class programa:
    def __init__(self):
        self.dato = True
    def menu(self):

        while self.dato:
            selection = input('\nSeleccione 1 para insertar, 2 para Actualizar, 3 para leer , 4 para eliminar o 5 para salir\n')

            if selection == '1':
                insert.insert()
            elif selection == '2':
                update.update()
            elif selection == '3':
                read.read()
            elif selection == '4':
                delete.delete()
            elif selection == '5':
                self.dato = False
            else:
                print('\n Selección Invalida\n')

programa1 = programa()
programa1.menu()