# Inserte comentarios

import sys
sys.path.append(".")
from logica.creadorMD import creadorMD
from logica.limpiar_BBDD import limpiar_BBDD
from acceso_a_datos.conector_BBDD import conector_cluster
from acceso_a_datos.conector_BBDD import acceder_BBDD


mongo_db_url = 'mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority'
# Llamamos a todas las funciones para conectarnos con mongodb

def proyecto_pydevops():
    
        client = conector_cluster(mongo_db_url)
        base_de_datos = acceder_BBDD(client)
        naves = limpiar_BBDD(base_de_datos)
        creadorMD(naves)
    

proyecto_pydevops() 