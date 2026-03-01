# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = username
        PASS = password
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT)) 
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data is not None: 
            try:
                self.database.animals.insert_one(data)  # data should be dictionary 
                return True
            except Exception as e:
                print("An error has occurred.")
                return False
        else: 
            raise Exception("Nothing to save, because data parameter is empty") 

    # Create method to implement the R in CRUD.
    def read(self, data):
        if data is not None:
            try:
                cursor = self.database.animals.find(data, {"_id": False})
                return list(cursor)
            except Exception as e:
                print("An error has occurred.")
                return []
        else:
            raise Exception("Nothing to find, because data parameter is empty")
            
    # Update method to implement the U in CRUD.
    def update(self, query, data):
        if data is not None:
            try:
                result = self.database.animals.update_may(query, data)
                return results.modified_count
            except Exception as e:
                print("An error has occurred.")
                return 0
        else:
            raise Exception("Nothing to find, because data parameter is empty")
            
    # Delete method to implement the D in CRUD.
    def delete(self, data):
        if data is not None:
            try:
                results = self.database.animals.delete_many(data)
                return results.deleted_count
            except Exception as e:
                print("An error has occurred.")
                return 0
        else:
            raise Exception("Nothing to find, because data parameter is empty")