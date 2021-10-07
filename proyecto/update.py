from pymongo import MongoClient

client = MongoClient()
db = client.EmployeeData

def update():
    try:
        criteria = input('\n Ingrese el ID del empleado a actualizar\n')
        employeename = input('Ingrese el nombre: ')
        employeeage = input('Ingrese la edad del empleado')
        employeecountry = input('Ingrese la ciudad del empleado')

        db.Employees.update_one({"id":criteria},
        {
            "$set":{
                "name":employeename,
                "age":employeeage,
                "country":employeecountry
            }
        })
        print('\n Datos actualizados exitosamente\n')

    except ImportError:
        plaform_specific_module = None

