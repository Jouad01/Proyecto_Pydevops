import pytest
import sys
sys.path.append(".")
from domain.src.logica.limpiar_BBDD import limpiar_BBDD
from pymongo import MongoClient

client = MongoClient('mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority')

BBDD = client.ProyectoPydevops.datos_naves.find()
@pytest.mark.limpiar_BBDD
def test_esta_limpia():
    for item in limpiar_BBDD(BBDD):
        for value in item:
            assert not value == "_id"
