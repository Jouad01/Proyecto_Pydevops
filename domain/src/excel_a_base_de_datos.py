from acceso_a_datos.acceder_a_formulario import acceder_a_formulario
from acceso_a_datos.agregador_base_de_datos import agregador_base_de_datos

def excel_a_base_de_datos():
    acceder_a_formulario()
    agregador_base_de_datos("naves.json")
if __name__ == "__main__":
    excel_a_base_de_datos()
