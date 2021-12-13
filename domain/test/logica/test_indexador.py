import sys
sys.path.append(".")
from  domain.src.logica.indexador_naves import indexador_naves
import pytest

@pytest.mark.indexador
def test_indexador():
    siguiente_nave = indexador_naves()
    siguiente_nave()
    siguiente_nave()
    siguiente_nave()
    assert siguiente_nave() == "nave4.md"