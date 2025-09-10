from app.connections.elasticsearch.elasticsearch_connection import ElasticConnection
from elasticsearch import Elasticsearch

class ElasticDal:
    def __init__(self, es:ElasticConnection):
        self._es = es.get_connection()




    def create_index(self, index, body = None):
        self._es.indices.delete(index=index)
        print(self._es.indices.create(index=index))


    # def refresh_index(self, index):
    #     self._es.indices.refresh(index=index)

    def insert_document(self, index, _id, document):
        response = self._es.index(index= index, id= _id ,body =document)

    def update_document(self, index, document_id, update_data):
        update_data = {'doc':update_data}
        response = self._es.update(index=index, id=document_id, body=update_data)

    def get_all_document(self, index) -> list:
        res = self._es.search(index=index, body={'query': {'match_all': {}}})
        return [doc['_source'] for doc in res['hits']['hits']]


















