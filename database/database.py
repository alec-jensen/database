from server import Server
from manager import Manager

class Database:
    def __init__(self) -> None:
        self.manager = Manager()
        self.server = Server(self.manager)
        self.server.start()

    def _verify_collection_name(self, collection: str):
        allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789-_"

        if not all(char in allowed_chars for char in collection.lower()):
            raise ValueError("Collection name contains invalid characters.")
    
    def _verify_document(self, document: dict):
        if not isinstance(document, dict):
            raise ValueError("Document must be a dictionary.")
        
        if "_id" in document:
            raise ValueError("Document cannot contain an _id field.")

    def fetch_one(self, collection: str, query: dict):
        self._verify_collection_name(collection)
        return self.manager.fetch_one(collection, query)
    
    def fetch_many(self, collection: str, query: dict, count: int):
        self._verify_collection_name(collection)
        return self.manager.fetch_many(collection, query, count)
    
    def insert_one(self, collection: str, document: dict):
        self._verify_collection_name(collection)
        self._verify_document(document)
        return self.manager.insert_one(collection, document)
    
    def insert_many(self, collection: str, documents: list):
        self._verify_collection_name(collection)
        for document in documents:
            self._verify_document(document)
        return self.manager.insert_many(collection, documents)
    
    def update_one(self, collection: str, query: dict, update: dict):
        self._verify_collection_name(collection)
        self._verify_document(update)
        return self.manager.update_one(collection, query, update)
    
    def delete_one(self, collection: str, query: dict):
        self._verify_collection_name(collection)
        return self.manager.delete_one(collection, query)
    
    def delete_many(self, collection: str, query: dict, count: int):
        self._verify_collection_name(collection)
        return self.manager.delete_many(collection, query, count)

if __name__ == "__main__":
    Database()
