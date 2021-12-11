import sys
sys.path.append(".")
from domain.logica.test.base_de_datos_ficticia import naves
from domain.logica.src.indexador_naves import indexador_naves
import os

def creadorMD(naves, nueva_linea = "\r"):
    siguiente_nave = indexador_naves() 
    for nave in naves:

        file = open("StarWays/content/post/" + siguiente_nave(), "w")
        file.write("+++" + nueva_linea)
        file.write("author = " + "'BobaFet'" + nueva_linea)
        file.write("title = " + "'" + nave['modelo'] + "'" + nueva_linea)
        file.write("date = '17-08-2002'" + nueva_linea)
        file.write("feature_image = '" + nave["img_url"] + "'" + nueva_linea)
        file.write("+++" + nueva_linea)
        file.write("<!--more--> " + nueva_linea)

        for element in nave:
            if isinstance(nave[element], list):
                insert_list(file, nave, element)
            else:
                insert_element(nave, file, element)
        file.close()

def insert_list(file, nave, element, nueva_linea = "\r"):
    file.write("# " + element + nueva_linea)
    for characteristic in nave[element]:
        file.write("* " + characteristic + nueva_linea)
    file.write(nueva_linea)

def insert_element(nave, file, element, nueva_linea = "\r"):
    if element[0:3] == "img":
        ""
    else:
        file.write(element + ": " + str(nave[element]) + nueva_linea + nueva_linea)

creadorMD(naves)