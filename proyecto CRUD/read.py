from platform import platform
from pymongo import MongoClient

client = MongoClient()
db = client.EmployeeData

def read():
    try:
        empcol = db.Employees.find()
        print('\n Toda la información de la base de empleados\n')
        for emp in empcol:
            print(emp)
    except ImportError:
        platform_specific_module = None