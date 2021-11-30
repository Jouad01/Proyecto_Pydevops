from base_de_datos_ficticia import naves
from indexador_naves import indexador_naves
import os

def creadorMD(naves):
    siguiente_nave = indexador_naves()
    for nave in naves:
        file = open(siguiente_nave, "w")
        