from app.connections.elasticsearch.elasticsearch_connection import ElasticConnection
from elasticsearch import Elasticsearch

class ElasticDal:
    def __init__(self, es:ElasticConnection, index, mapping = None):
        self._es = es
        self.create_index(index, mapping)


    def create_index(self, index, body = None):
        self._es.indices.delete(index=index)
        self._es.indices.create(index=index, body=body)

    # def refresh_index(self, index):
    #     self._es.indices.refresh(index=index)

    def insert_document(self, index, document):
        pass
















