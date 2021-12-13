# Inserte comentarios

import sys
sys.path.append(".")
from domain.logica.src.creadorMD import creadorMD
from domain.logica.src.limpiar_BBDD import limpiar_BBDD
from domain.acceso_a_datos.src.conector_BBDD import conector_cluster
from domain.acceso_a_datos.src.conector_BBDD import acceder_BBDD

# Llamamos a todas las funciones para conectarnos con mongodb

def proyecto_pydevops():
    client = conector_cluster()
    base_de_datos = acceder_BBDD(client)
    naves = limpiar_BBDD(base_de_datos)
    creadorMD(naves)

proyecto_pydevops()