from pymongo import MongoClient
from pprint import pprint

def insertarUno(nave):
    cliente = MongoClient('mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/ProyectoPydevops?retryWrites=true&w=majority')
    db = cliente('ProyectoPydevops')
    
    doc = {'modelo':nave['modelo'],'marca':nave['marca'],'gama':nave['gama'], 'tasa':nave['tasa'], 'color':nave['color'], 'plazas':nave['plazas'], 'caracteristicas':nave['caracteristicas']}

    compr = {'modelo':doc['modelo']}
    
    if documentos.count() == 0:
        #Si no existe ningún documento igual, lo genera
        db.datos_naves.insert_one(doc)
        print(" ")
        print("Servicio guardado:")
        #Muestra el documento generado estructuradamente
        pprint(doc)
    else:
        #Si ya existe un documento, entonces actualiza el documento existente con los datos recogidos
        print(" ")
        print("Servicio actualizado:")
        db.datos_naves.update_one(compr,{"$set":doc})
        #Muestra el documento generado estructuradamente
        pprint(doc)
