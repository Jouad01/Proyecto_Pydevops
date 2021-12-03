from pymongo import MongoClient

def conector_BBDD():
    client = MongoClient('localhost')
    print (client.list_database_names())

conector_BBDD()

