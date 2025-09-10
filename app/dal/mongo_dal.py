
from app.connections.mongo_db.mongo_connection import MongoConnection


class MongoDal:
    def __init__(self, db:MongoConnection):
        self.db = db.get_db()


    def insert_document(self, collection_name, document):
        self.db[collection_name].insert_one(document)
        # document['_id'] = str(result.inserted_id)
        # return document

    def get_all_documents(self, collection_name) -> list:
        """List all document in the database."""
        return list(self.db[collection_name].find())