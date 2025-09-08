from pymongo import ASCENDING

from app.connections.mongo_db.mongo_connection import MongoConnection


class MongoDal:
    def __init__(self, db: MongoConnection):
        self.db = db


    async def insert_document(self, collection_name, document):
        result = await self.db.get_db_collection(collection_name).insert_one(document)
        document['_id'] = str(result.inserted_id)
        return document
