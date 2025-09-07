from importlib.metadata import metadata
#
from app.models import Producer
from app.services.data_retrieval.conigurations import JSON_SCHEMA, KAFKA_TOPIC, DIRECTORY_PATH, FILE_PATH_TEMPLATE
from app.services.data_retrieval.data_retrieval_manager import DataRetrievalManager


class DataRetrievalService:
    def __init__(self):
        self._directory_path = DIRECTORY_PATH
        self._file_path_template = FILE_PATH_TEMPLATE
        self._kafka_topic = KAFKA_TOPIC
        self._producer = Producer()
        self._manager = DataRetrievalManager()


    def send_metadata(self):
        for i in range(self._manager.get_count_files(self._directory_path)):
            specific_meta_data = self._manager.get_metadata(self._file_path_template.replace('%', str(i)))
            self._producer.publish_massage(self._kafka_topic, specific_meta_data)




