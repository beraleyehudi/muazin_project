from app.services import SUCCESSFUL_SENDING, DELIVERY_FAILED
from app.services.logging.logger import Logger
from app.connections.mongo_db.mongo_connection import MongoConnection


class MongoDal:
    def __init__(self, db: MongoConnection):
        self._db = db
        self._logger = Logger.get_logger()


    def insert_document(self, collection_name, document):
        try:
            self._db.get_db_collection(collection_name).insert_one(document)
            self._logger.info(SUCCESSFUL_SENDING.replace('$', 'mongo_db'))
        except:
            self._logger.error(DELIVERY_FAILED.replace('$', 'mongo_db'))

        # document['_id'] = str(result.inserted_id)
        # return document
