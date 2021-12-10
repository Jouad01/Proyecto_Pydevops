# Importante usar 'import sys' cuando vamos a importar ficheros de otros directorios
import sys
sys.path.append(".")
from domain.logica.test.base_de_datos_ficticia import naves
from domain.logica.src.indexador_naves import indexador_naves
import os

# Tres funciones para crear automáticamente el markdown como nosotros queremos

# Con esta se crea el formato markdown
def creadorMD(naves, nueva_linea="\n"):
    siguiente_nave = indexador_naves()
    for nave in naves:
        # Especificamos como queremos que sea nuestro hugo generado 
                    # Usamos el encoding para que el markdown lea los caracters diferentes
        file = open("StarWays/content/post/" + siguiente_nave(), "w", encoding="utf-8")
        file.write("+++" + "\n")
        file.write("author = " + "'BobaFet'" + "\n" + nueva_linea)
        file.write("title = " + "'" + nave['modelo'] + "'" + "\n")
        file.write("date = '17-08-2002'" + "\n")
        file.write("feature_image = '" + nave["img_url"] + "'" + "\n")
        file.write("+++" + "\n")
        file.write("<!--more--> " + "\n")

        for element in nave:
            if isinstance(nave[element], list):
                insert_list(file, nave, element)
            else:
                insert_element(nave, file, element)
        file.close()

# Con esta nos aseguramos que nos pone lo que queremos como título y en una lista no ordenada
def insert_list(file, nave, element):
    file.write("# " + element + "\n")
    for characteristic in nave[element]:
        file.write("* " + characteristic + "\n")
    file.write("\n")

# Con esta función podemos generar las imágenes dentro del markdown.
def insert_element(nave, file, element):
    if element[0:3] == "img":
        ""
    else:
        file.write(element + ": " + str(nave[element]) + "\n" + "\n")

# Eliminar esto
