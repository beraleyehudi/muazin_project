from app.services.data_loader.data_loader_manager import DataLoaderManager


class DataLoaderService:
    def __init__(self):
        self._kafka_read_topic = ''
        self._manager = DataLoaderManager

