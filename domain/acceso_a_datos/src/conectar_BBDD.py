# En caso de un SO Windows hay que importar el certifi
import certifi
from pymongo import MongoClient

# Función para conectarnos con nuestra BBDD
def conector_cluster():
    
    # Importante tener en cuenta para Windows el 'ce = certifi.where()'
    ca = certifi.where()
    # Al final del enlace, para sistemas windows, hay que agregar 'tlsCAFile=ca'
    client = MongoClient('mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority', tlsCAFile=ca)

    return client

def acceder_BBDD(client):
    base_de_datos = client.ProyectoPydevops.datos_naves.find()
    return base_de_datos

