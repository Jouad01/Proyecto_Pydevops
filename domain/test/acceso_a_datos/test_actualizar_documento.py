import pytest
import sys
sys.path.append(".")
from domain.src.acceso_a_datos.actualizar_documento import actualizar_documento

mongo_db_url = "mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority"

@pytest.mark.actualizar_base_de_datos
def test_actualizar_base_de_datos():   
    assert actualizar_documento(mongo_db_url, {"modelo":"Destructor Estelar clase Venator"}, {"tasa":1500})
print(actualizar_documento(mongo_db_url, {"modelo":"Destructor Estelar clase Venator"}, {"tasa":1500}))