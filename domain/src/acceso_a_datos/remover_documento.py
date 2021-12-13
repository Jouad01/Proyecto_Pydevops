import pymongo
import sys
sys.path.append(".")
from domain.src.acceso_a_datos.conector_BBDD import conector_cluster

mongo_db_url = 'mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority'

def remover_docmumento(mongo_db_url, elemento_a_borrar):
    try:
        client = conector_cluster(mongo_db_url)
        BBDD = client.ProyectoPydevops.datos_naves
    except:
        print("ingrese una base de datos correcta")
        return False
    try:
        BBDD.delete_one(elemento_a_borrar)
        print("elemento borrado correctamente")
    except:
        print("documento o base de datos incorrecta")
        return False
    return True

if __name__ == "__main__":
    remover_docmumento(mongo_db_url, {"modelo":"Destrur Estelar clase Venator"})
    