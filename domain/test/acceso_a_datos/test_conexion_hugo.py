import pytest
import sys
sys.path.append(".")
from domain.src.acceso_a_datos.conector_BBDD import conector_cluster
from domain.src.acceso_a_datos.conector_BBDD import acceder_BBDD
print("hola")
url_correcta = 'mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority'

url_incorrecta = "XD"
@pytest.mark.BBDD_connection
def test_url_correcta():
    cluster = conector_cluster(url_correcta)
    assert acceder_BBDD(cluster)
#Si la base de datos no existe, devolverá false
@pytest.mark.BBDD_connection
def test_url_incorrecta():
    cluster = conector_cluster(url_incorrecta)
    assert not acceder_BBDD(cluster)

