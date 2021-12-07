# Importante importar sys para el markdown.
import sys
sys.path.append(".")
from domain.logica.test.base_de_datos_ficticia import naves
from domain.logica.src.indexador_naves import indexador_naves
import os

# Tres funciones para crear automáticamente el markdown como nosotros creamos

# Con esta se crea el formato markdown
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

# Con esta nos aseguramos que nos pone lo que queremos como título y en una lista no ordenada
def insert_list(file, nave, element):
    file.write("# " + element + os.linesep)
    for characteristic in nave[element]:
        file.write("* " + characteristic + os.linesep)
    file.write(os.linesep)

# Con esta función podemos generar las imágenes dentro del markdown.
def insert_element(nave, file, element):
    if element[0:3] == "img":
        file.write("![](" + str(nave[element] + ")") + os.linesep + os.linesep)
    else:
        file.write(element + ": " + str(nave[element]) + os.linesep + os.linesep)

# Eliminar esto
creadorMD(naves)