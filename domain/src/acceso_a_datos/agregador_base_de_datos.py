import pymongo
import json
def agregador_base_de_datos():
    
    myclient = pymongo.MongoClient("mongodb+srv://devops:12345@proyectopydevops.gk2qp.mongodb.net/ProyectoPydevops?retryWrites=true&w=majority")
    naves = myclient.ProyectoPydevops.datos_naves
    with open('naves.json') as json_file: 
        nave = json.load(json_file) 
    for element in nave:
        if nave[element].isnumeric() == True:
            nave[element] = int(nave[element])
        if element.strip() == "caracteristicas":
            nave[element] = nave[element].split(", ")
    
    x = naves.insert_one(nave)
    print("se ha insertado correctamente el objeto con id " + str(x))   

if __name__ == "__main__":
    agregador_base_de_datos()