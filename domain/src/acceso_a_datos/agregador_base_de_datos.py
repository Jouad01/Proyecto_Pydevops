import pymongo
import json
def agregador_base_de_datos(nueva_nave):
    try:
        myclient = pymongo.MongoClient("mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/ProyectoPydevops?retryWrites=true&w=majority")
        naves = myclient.ProyectoPydevops.datos_naves
        with open(nueva_nave) as json_file: 
            nave = json.load(json_file) 
        for element in nave:
            if nave[element].isnumeric() == True:
                nave[element] = int(nave[element])
            if element.strip() == "caracteristicas":
                nave[element] = nave[element].split(", ")
    
        naves.insert_one(nave)
        print("se ha insertado correctamente la nave")   
        return True
    except:
        return False
if __name__ == "__main__":
    agregador_base_de_datos("naves.json")