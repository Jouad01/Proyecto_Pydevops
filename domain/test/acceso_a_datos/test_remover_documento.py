import sys
sys.path.append(".")
from domain.src.acceso_a_datos.remover_documento import remover_docmumento
import pytest
mongo_db_url = 'mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/?retryWrites=true&w=majority'

@pytest.mark.remover_documento
def test_documento_existe():   
    assert remover_docmumento(mongo_db_url, {"modelo":"Spam"})
@pytest.mark.remover_documento
def test_documento_no_existe():   
    assert not remover_docmumento("mongodb+srv://devops:12345@proyectopyvops.gk2qp.mongodb.net/?retryWrites=true&w=majority", {"modelo":"Spam"})