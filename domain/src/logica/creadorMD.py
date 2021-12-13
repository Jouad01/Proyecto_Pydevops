# Importante usar 'import sys' cuando vamos a importar ficheros de otros directorios
import sys

sys.path.append(".")
from domain.test.logica.base_de_datos_ficticia import naves
from logica.indexador_naves import indexador_naves


# Tres funciones para crear automáticamente el markdown como nosotros queremos

# Con esta se crea el formato markdown

def creadorMD(naves, nueva_linea="\n"):
    siguiente_nave = indexador_naves()
    for nave in naves:
        # Especificamos como queremos que sea nuestro hugo generado
        file = open("domain/src/StarWays/content/post/" + siguiente_nave(), "w", encoding="utf8")
        insert_metadatos(nave, file)

        for element in nave:
            if isinstance(nave[element], list):
                insert_list(file, nave, element)
            else:
                insert_element(nave, file, element)
        file.close()


# Con esta nos aseguramos que nos pone lo que queremos como título y en una lista no ordenada
def insert_list(file, nave, element, nueva_linea="\n"):
    file.write("# " + element + nueva_linea)
    for characteristic in nave[element]:
        file.write("* " + characteristic + nueva_linea)
    file.write(nueva_linea)


# Con esta función podemos generar las imágenes dentro del markdown.
def insert_element(nave, file, element, nueva_linea="\n"):
    if element[0:3] == "img":
        ""
    else:
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
if __name__ == "__main__":
    creadorMD(naves)
