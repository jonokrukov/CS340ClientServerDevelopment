from pymongo import MongoClient

class CRUD(object):
    # CRUD operations for MongoDB
    
    def __init__(self, username, password, host, port, db, collection):
        # Initializes MongoDB connection
        self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/")
        self.db = self.client[db]
        self.collection = self.db[collection]
        
    def create(self, data):
        # Inserts document(s) into collection
        try:
            self.collection.insert_one(data)
            return True
        except Exception as e:
            print(f"Error creating document: {e}")
            return False
    
    def read(self, query):
        # Reads document(s) from collection
        try:
            result = list(self.collection.find(query))
            return result
        except Exception as e:
            print(f"Error reading document: {e}")
            return[]
        
    def update(self, query, updated_Data):
        # Updates document(s) from collection
        try:
            result = self.collection.update_many(query, {"$set": updated_Data})
            return result.modified_count
        except Exception as e:
            print(f"Error updating document: {e}")
            return 0
    
    def delete(self, query):
        # Deletes document(s) from collection
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting document: {e}")
            return 0