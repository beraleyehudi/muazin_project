from app.connections import Consumer
from app.connections.elasticsearch.elasticsearch_connection import ElasticConnection
from app.connections.mongo_db.mongo_connection import MongoConnection
from app.dal import MongoDal
from app.dal.elastic_dal import ElasticDal
from app.services.data_loader.configurations import *
from app.services.data_loader.data_loader_helper import DataLoaderHelper


class DataLoaderService:
    def __init__(self):
        self._helper = DataLoaderHelper
        self._kafka_read_topic = KAFKA_READ_TOPIC
        self._elastic_mapping = ELASTIC_MAPPING
        self._collection_name = COLLECTION_NAME
        self._consumer = Consumer(self._kafka_read_topic)
        self._elastic_dal = ElasticDal(ElasticConnection.get_connection(), self._collection_name, self._elastic_mapping)
        self._mongo_dal = MongoDal(MongoConnection())


    def insert_to_mongo(self, unique_id, file_path):
        proper_mongo_object = self._helper.convert_audio_to_mongo_proper_object(file_path)
        document = {'id': unique_id, 'audio': proper_mongo_object}
        self._mongo_dal.insert_document(self._collection_name, document)



    def insert_into_elastic(self, document):
        self._elastic_dal.insert_document(self._collection_name, document)

    def load_data(self):
        for message in self._consumer.get_consumed_messages():
            document = message.value
            unique_id = self._helper.calculate_unique_id(document)
            document['id'] = unique_id
            self.insert_into_elastic(document)
            self.insert_to_mongo(unique_id, document.get('path'))









