import sys
sys.path.append(".")
from domain.src.acceso_a_datos.agregador_base_de_datos import agregador_base_de_datos
import pytest

@pytest.mark.agregador_base_de_datos
def test_documento_correcto():   
    assert agregador_base_de_datos("test.json")
@pytest.mark.agregador_base_de_datos
def test_documento_incorrecto():   
    assert not agregador_base_de_datos("ns.json")