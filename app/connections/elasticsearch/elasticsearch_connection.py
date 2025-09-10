from elasticsearch import Elasticsearch
import os
class ElasticConnection:
    _es = None

    @classmethod
    def get_connection(cls):
        if not cls._es:
            cls._es = Elasticsearch(os.environ['ELASTICSEARCH_HOST'])
        return cls._es


