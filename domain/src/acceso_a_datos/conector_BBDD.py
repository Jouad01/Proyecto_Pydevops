# En caso de un SO Windows hay que importar el certifi
import certifi
from pymongo import MongoClient

mongo_db_url = 'mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority'
# Función para conectarnos con nuestra BBDD
def conector_cluster(mongo_db_url):
    try:
        # Importante tener en cuenta para Windows el 'ce = certifi.where()'
        ca = certifi.where()
        # Al final del enlace, para sistemas windows, hay que agregar 'tlsCAFile=ca'
        client = MongoClient(mongo_db_url, tlsCAFile=ca)
        return client
    except:
        print("el servidor esta caido o la url es incorrecta")
        return False 
def acceder_BBDD(client):
    try:
        base_de_datos = client.ProyectoPydevops.datos_naves.find()
        naves = []
        for item in base_de_datos:
            naves.append(item)
        return naves
    except:
        print("el servidor esta caido o la url es incorrecta")
        return False
        