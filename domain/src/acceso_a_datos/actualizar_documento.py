import sys
sys.path.append(".")
from domain.src.acceso_a_datos.conector_BBDD import conector_cluster
import pymongo

mongo_db_url = 'mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority'

def actualizar_documento(mongo_db_url, elementmo_a_modificar, modificacion,):
    client = conector_cluster(mongo_db_url)
    try:
        BBDD = client.ProyectoPydevops.datos_naves
    except:
        print("ingrese una base de datos correcta")
        return False
    try:
        BBDD.update_one(elementmo_a_modificar, {"$set": modificacion})
    except:
        print("ingrese una peticion correcta")
        return False
    return True

if __name__ == "__main__":
    actualizar_documento(mongo_db_url, {"modelo":"Destructor Estelar clase Venator"}, {"tasa":1250})
    actualizar_documento(mongo_db_url, {"nombre" : "destructor estelar"}, {"nombre":"destructor"})