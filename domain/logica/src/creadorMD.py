# Importante usar 'import sys' cuando vamos a importar ficheros de otros directorios
import sys

sys.path.append(".")
from domain.logica.test.base_de_datos_ficticia import naves
from domain.logica.src.indexador_naves import indexador_naves
import os


# Tres funciones para crear automáticamente el markdown como nosotros queremos

# Con esta se crea el formato markdown

def creadorMD(naves, nueva_linea="\r"):
    siguiente_nave = indexador_naves()
    for nave in naves:
        # Especificamos como queremos que sea nuestro hugo generado
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


# Con esta nos aseguramos que nos pone lo que queremos como título y en una lista no ordenada
def insert_list(file, nave, element, nueva_linea="\r"):
    file.write("# " + element + nueva_linea)
    for characteristic in nave[element]:
        file.write("* " + characteristic + nueva_linea)
    file.write(nueva_linea)


# Con esta función podemos generar las imágenes dentro del markdown.
def insert_element(nave, file, element, nueva_linea="\r"):
    if element[0:3] == "img":
        ""
    else:
        file.write(element + ": " + str(nave[element]) + nueva_linea + nueva_linea)


# Eliminar esto
creadorMD(naves)
