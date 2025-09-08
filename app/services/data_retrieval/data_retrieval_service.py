import os
from app.connections import Producer

from app.services.data_retrieval.conigurations import JSON_SCHEMA, KAFKA_TOPIC, DIRECTORY_PATH
from app.services.data_retrieval.data_retrieval_helper import DataRetrievalHelper



class DataRetrievalService:
    def __init__(self):
        self._directory_path = DIRECTORY_PATH
        self._kafka_topic = KAFKA_TOPIC
        self._producer = Producer()
        self._manager = DataRetrievalHelper


    def send_metadata(self):

        for entry in os.listdir(self._directory_path):
            specific_meta_data = self._manager.get_specific_metadata(os.path.join(self._directory_path, entry))
            print(specific_meta_data)
            self._producer.publish_massage(self._kafka_topic, specific_meta_data)



DataRetrievalService().send_metadata()
