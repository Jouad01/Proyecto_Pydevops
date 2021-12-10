# Importante usar 'import sys' cuando vamos a importar ficheros de otros directorios
import sys
sys.path.append(".")
from domain.logica.test.base_de_datos_ficticia import naves
from domain.logica.src.indexador_naves import indexador_naves
import os

# Tres funciones para crear automáticamente el markdown como nosotros queremos

# Con esta se crea el formato markdown
def creadorMD(naves):
    siguiente_nave = indexador_naves()
    for nave in naves:
        # Especificamos como queremos que sea nuestro hugo generado
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

# Con esta nos aseguramos que nos pone lo que queremos como título y en una lista no ordenada
def insert_list(file, nave, element):
    file.write("# " + element + os.linesep)
    for characteristic in nave[element]:
        file.write("* " + characteristic + os.linesep)
    file.write(os.linesep)

# Con esta función podemos generar las imágenes dentro del markdown.
def insert_element(nave, file, element):
    if element[0:3] == "img":
        ""
    else:
        file.write(element + ": " + str(nave[element]) + os.linesep + os.linesep)

# Eliminar esto
creadorMD(naves)