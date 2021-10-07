from pymongo import MongoClient

client = MongoClient()
db = client.EmployeeData

def insert():
    try:
        employeeid = input('Ingrese el ID del empleado: ')
        employeename = input('Ingrese el nombre: ')
        employeeage = input('Ingrese la edad del empleado')
        employeecountry = input('Ingrese la ciudad del empleado')
        db.Employees.insert(
        {
            "id":employeeid,
            "name":employeename,
            "age":employeeage,
            "country":employeecountry

        })
        print('Empleado insertado con exito')
    except ImportError:
        plaform_specific_module = None
