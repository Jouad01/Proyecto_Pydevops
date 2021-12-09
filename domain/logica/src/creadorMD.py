import sys
sys.path.append(".")
from domain.logica.test.base_de_datos_ficticia import naves
from domain.logica.src.indexador_naves import indexador_naves
import os

def creadorMD(naves):
    siguiente_nave = indexador_naves()

    for nave in naves:

        file = open("StarWays/content/post/" + siguiente_nave(), "w")
        file.write("+++" + os.linesep)
        file.write("author = " + "'BobaFet'" + os.linesep)
        file.write("title = " + "'" + nave['modelo'] + "'" + os.linesep)
        file.write("date = '17-08-2002'" + os.linesep)
        file.write("feature_image = '" + nave["img_url"] + "'" + os.linesep)
        file.write("+++" + os.linesep)
        file.write("<!--more--> " + os.linesep)

        for element in nave:
            if isinstance(nave[element], list):
                insert_list(file, nave, element)
            else:
                insert_element(nave, file, element)
        file.close()

def insert_list(file, nave, element):
    file.write("# " + element + os.linesep)
    for characteristic in nave[element]:
        file.write("* " + characteristic + os.linesep)
    file.write(os.linesep)

def insert_element(nave, file, element):
    if element[0:3] == "img":
        ""
    else:
        file.write(element + ": " + str(nave[element]) + os.linesep + os.linesep)

creadorMD(naves)