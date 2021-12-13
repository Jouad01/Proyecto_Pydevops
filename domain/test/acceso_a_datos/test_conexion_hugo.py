import pytest
from src.conector_BBDD import conector_cluster
from src.conector_BBDD import acceder_BBDD
url_correcta = 'mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority'
url_incorrecta = "XD"
@pytest.mark.BBDD_connection
def test_url_correcta():
    cluster = conector_cluster(url_correcta)
    assert acceder_BBDD(cluster)
#Si la base de datos no existe, enviará un puntero vacío, por lo que le generará una pagina web vacía
@pytest.mark.BBDD_connection
def test_url_incorrecta():
    cluster = conector_cluster(url_incorrecta)
    assert acceder_BBDD(cluster)

