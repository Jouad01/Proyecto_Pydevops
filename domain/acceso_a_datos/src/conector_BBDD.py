from pymongo import MongoClient

def conector_cluster():
    client = MongoClient("mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/ProyectoPydevops?retryWrites=true&w=majority")
    return client
def acceder_BBDD(client):
    base_de_datos = client.ProyectoPydevops.datos_naves.find()
    return base_de_datos
