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
<<<<<<< HEAD
        # Especificamos como queremos que sea nuestro hugo generado 
                    # Usamos el encoding para que el markdown lea los caracters diferentes
        file = open("StarWays/content/post/" + siguiente_nave(), "w", encoding="utf-8")
        file.write("+++" + "\n")
        file.write("author = " + "'BobaFet'" + "\n")
        file.write("title = " + "'" + nave['modelo'] + "'" + "\n")
        file.write("date = '17-08-2002'" + "\n")
        file.write("feature_image = '" + nave["img_url"] + "'" + "\n")
        file.write("+++" + "\n")
        file.write("<!--more--> " + "\n")
=======
        # Especificamos como queremos que sea nuestro hugo generado
        file = open("domain/StarWays/content/post/" + siguiente_nave(), "w", encoding="utf8")
        insert_metadatos(nave, file)
>>>>>>> d8efa9a536f653f06b52637186f8d62b5acb4bed

        for element in nave:
            if isinstance(nave[element], list):
                insert_list(file, nave, element)
            else:
                insert_element(nave, file, element)
        file.close()


# Con esta nos aseguramos que nos pone lo que queremos como título y en una lista no ordenada
<<<<<<< HEAD
def insert_list(file, nave, element):
    file.write("# " + element + "\n")
    for characteristic in nave[element]:
        file.write("* " + characteristic + "\n")
    file.write("\n")
=======
def insert_list(file, nave, element, nueva_linea="\n"):
    file.write("# " + element + nueva_linea)
    for characteristic in nave[element]:
        file.write("* " + characteristic + nueva_linea)
    file.write(nueva_linea)

>>>>>>> d8efa9a536f653f06b52637186f8d62b5acb4bed

# Con esta función podemos generar las imágenes dentro del markdown.
def insert_element(nave, file, element, nueva_linea="\n"):
    if element[0:3] == "img":
        ""
    else:
<<<<<<< HEAD
        file.write(element + ": " + str(nave[element]) + "\n" + "\n")

# Eliminar esto
=======
        file.write(element + ": " + str(nave[element]) + nueva_linea + nueva_linea)
# Con esta función creamos los metadatos necesarios para enlazar las paginas de hugo y que se generen los posts correctamente
def insert_metadatos(nave, file, nueva_linea ="\n"):
    file.write("+++" + nueva_linea)
    file.write("author = " + "'BobaFet'" + nueva_linea)
    file.write("title = " + "'" + nave['modelo'] + "'" + nueva_linea)
    file.write("date = '17-08-2002'" + nueva_linea)
    file.write("feature_image = '" + nave["img_url"] + "'" + nueva_linea)
    file.write("tags = ['Gama: " + nave["gama"].lower() + "']" + nueva_linea)
    file.write("+++" + nueva_linea)
    file.write("<!--more--> " + nueva_linea)
        

# Eliminar esto
creadorMD(naves)
>>>>>>> d8efa9a536f653f06b52637186f8d62b5acb4bed
