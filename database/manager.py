import os
import json
from uuid import uuid4

# TODO: parse operator in query

class Manager:
    def __init__(self):
        if not os.path.exists("data"):
            os.mkdir("data")

        if not os.path.isfile("data/config.json"):
            with open("data/config.json", "w") as f:
                f.write("{}")
        
        if not os.path.isfile("data/access.json"):
            with open("data/access.json", "w") as f:
                f.write("{}")

    def fetch_one(self, collection: str, query: dict):
        if not os.path.exists(f"data/{collection}"):
            os.makedirs(f"data/{collection}")

        for file in os.listdir(f"data/{collection}"):
            with open(f"data/{collection}/{file}", "r") as f:
                document = json.load(f)

                for key, value in query.items():
                    if document.get(key) != value:
                        break
                else:
                    return document
                
        return None
    
    def fetch_many(self, collection: str, query: dict, count: int):
        if not os.path.exists(f"data/{collection}"):
            os.makedirs(f"data/{collection}")

        documents = []

        for file in os.listdir(f"data/{collection}"):
            with open(f"data/{collection}/{file}", "r") as f:
                document = json.load(f)

                for key, value in query.items():
                    if document.get(key) != value:
                        break
                else:
                    documents.append(document)
                
                if len(documents) >= count:
                    break
        
        return documents

    def insert_one(self, collection: str, document: dict):
        if not os.path.exists(f"data/{collection}"):
            os.makedirs(f"data/{collection}")

        uuid = str(uuid4())

        document["_id"] = uuid

        if self.fetch_one(collection, {"_id": uuid}) is not None:
            return

        with open(f"data/{collection}/{uuid}.json", "w") as f:
            json.dump(document, f)

    def insert_many(self, collection: str, documents: list):
        for document in documents:
            self.insert_one(collection, document)

    def update_one(self, collection: str, query: dict, update: dict):
        doc = self.fetch_one(collection, query)

        if doc is None:
            return
        
        for key, value in update.items():
            doc[key] = value

        with open(f"data/{collection}/{doc['_id']}.json", "w") as f:
            json.dump(doc, f)

    def delete_one(self, collection: str, query: dict):
        if not os.path.exists(f"data/{collection}"):
            os.makedirs(f"data/{collection}")

        for file in os.listdir(f"data/{collection}"):
            with open(f"data/{collection}/{file}", "r") as f:
                document = json.load(f)

            for key, value in query.items():
                if document.get(key) != value:
                    break
            else:
                os.remove(f"data/{collection}/{file}")
                break

    def delete_many(self, collection: str, query: dict, count: int):
        if not os.path.exists(f"data/{collection}"):
            os.makedirs(f"data/{collection}")

        deleted = 0

        for file in os.listdir(f"data/{collection}"):
            with open(f"data/{collection}/{file}", "r") as f:
                document = json.load(f)

            for key, value in query.items():
                if document.get(key) != value:
                    break
            else:
                os.remove(f"data/{collection}/{file}")
                deleted += 1

            if deleted >= count:
                break
