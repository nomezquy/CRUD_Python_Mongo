from pymongo import MongoClient
from pymongo import collection

client = MongoClient()
db= client.mystore
coll = db.products
producto = {"Name": "Keyboard","Price":10000} ## ejemplo de documento a almacenar
coll.insert(producto) ## Insertando un documento en la db mystore y colleccion products

