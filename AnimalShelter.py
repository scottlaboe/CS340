from pymongo import MongoClient
from bson.objectid import ObjectId
import urllib.parse

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username=None, password=None):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        #username = urllib.parse.quote_plus('accuser')
        #password = urllib.parse.quote_plus('password')
        if username and password:
            uri = "mongodb://%s:%s@localhost:41742/?authSource=AAC&authMechanism=SCRAM-SHA-1" % (username, password)
            self.client = MongoClient(uri)
            self.database = self.client['AAC']
        else:
            print("ERROR: Must supply a username and password to instantiate AnimalShelter")

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animal.insert_one(data)  # data should be dictionary
            
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Create method to implement the R in CRUD. 
    def read(self, data=None):
        if data:
            animals = self.database.animal.find(data, {"_id":False})
        else:
            animals = self.database.animal.find({}, {"_id":False})
        
        return animals
    
    def update(self, field, data):
        status = self.database.animal.update_many(field, {'$set': data})
        return status.matched_count
            
    def delete(self, data):
        status = self.database.animal.delete_many(data)
        return status.deleted_count
