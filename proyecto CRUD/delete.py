from pymongo import MongoClient

client = MongoClient()
db = client.EmployeeData
coll = db.Employees

def delete():
    try:
        criteria = input('\n Ingrese el Id a eliminar\n')
        coll.delete_many({"id":criteria})
        print('\n Se eliminó correctamente\n')
    except ImportError:
        plaform_specific_module = None