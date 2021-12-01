from base_de_datos_ficticia import naves
from indexador_naves import indexador_naves
import os

def creadorMD(naves):
    siguiente_nave = indexador_naves()
    for nave in naves:
        file = open("supuesto_hugo/posts/" + siguiente_nave(), "w")
        for element in nave:
            if isinstance(nave[element], list):
                insert_list(file, nave, element)
            else:
                insert_element(nave, file, element)
        file.close()

def insert_list(file, nave, element):
    file.write("# " + element + os.linesep)
    for characteristic in nave[element]:
        file.write("- " + characteristic + os.linesep)

def insert_element(nave, file, element):
    file.write(element + ": " + str(nave[element]) + os.linesep + os.linesep)

creadorMD(naves)