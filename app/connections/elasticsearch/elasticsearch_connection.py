from elasticsearch import Elasticsearch
class ElasticConnection:
    _es = None

    @classmethod
    def get_connection(cls):
        if not cls._es:
            cls._es = Elasticsearch('http://localhost:9200')
        return cls._es


