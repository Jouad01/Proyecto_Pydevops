# Inserte comentarios

from os import name
import sys
sys.path.append(".")
sys.path.append(".")
from domain.src.logica.creadorMD import creadorMD
from domain.src.logica.limpiar_BBDD import limpiar_BBDD
from domain.src.acceso_a_datos.conector_BBDD import conector_cluster
from domain.src.acceso_a_datos.conector_BBDD import acceder_BBDD


mongo_db_url = 'mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority'
# Llamamos a todas las funciones para conectarnos con mongodb

def proyecto_pydevops(mongo_db_url):

        client = conector_cluster(mongo_db_url)
        base_de_datos = acceder_BBDD(client)
#        if base_de_datos == False:
#                exit()
        naves = limpiar_BBDD(base_de_datos)
        creadorMD(naves)

if __name__ == "__main__":
        proyecto_pydevops(mongo_db_url) 