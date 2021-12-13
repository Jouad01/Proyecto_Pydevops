<<<<<<< HEAD
# Añadimos el json a la base de datos
=======
>>>>>>> d8efa9a536f653f06b52637186f8d62b5acb4bed
import pymongo
import json
myclient = pymongo.MongoClient("mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/ProyectoPydevops?retryWrites=true&w=majority")
naves = myclient.ProyectoPydevops.datos_naves
with open('naves.json') as json_file: 
    nave = json.load(json_file) 
x = naves.insert_one(nave)
print("se ha insertado correctamente el objeto con id " + str(x))