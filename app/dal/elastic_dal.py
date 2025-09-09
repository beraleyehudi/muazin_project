from app.connections.elasticsearch.elasticsearch_connection import ElasticConnection
from elasticsearch import Elasticsearch

class ElasticDal:
    def __init__(self, es:ElasticConnection):
        self._es = es.get_connection()




    def create_index(self, index, body = None):
        self._es.indices.delete(index=index)
        self._es.indices.create(index=index, body=body)

    # def refresh_index(self, index):
    #     self._es.indices.refresh(index=index)

    def insert_document(self, index, _id, document):
        response = self._es.index(index= index, id= _id ,body =document)

    def update_document(self, index, document_id, update_data):
        update_data = {'doc':update_data}
        response = self._es.update(index=index, id=document_id, body=update_data)


















