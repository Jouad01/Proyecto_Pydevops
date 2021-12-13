from  src.main import proyecto_pydevops
import pytest

@pytest.mark.dependencias
def test_dependencias_correctas():
    assert proyecto_pydevops()
@pytest.mark.dependencias
def test_falta_dependencia():
    assert not proyecto_pydevops()