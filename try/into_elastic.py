from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')
my_index = 'test'
document = {'name':'berale', 'age':'24'}
es.indices.delete(index=my_index)
es.indices.create(index=my_index)
print(es.index(index='test', id='22', body=document))

class ElasticConnection:
    _es = None

    @classmethod
    def get_connection(cls):
        if not cls._es:
            cls._es = Elasticsearch('http://localhost:9200')
        return cls._es



class ElasticDal:
    def __init__(self, ess:ElasticConnection):
        self._es = ess.get_connection()




    def create_index(self, index, body = None):
        self._es.indices.delete(index=index)
        self._es.indices.create(index=index)
        self.refresh_index(index)
        print('created')

    def refresh_index(self, index):
        self._es.indices.refresh(index=index)

    def insert_document(self, index, id, document):
        print(self._es.index(index=index, id=id, body=document))


class Test:
    def __init__(self):
        self._elastic_dal = ElasticDal(ElasticConnection())


    def insert_into_elastic(self, document, id):
        self._elastic_dal.create_index('audio')
        self._elastic_dal.insert_document('audio', document, id)


# ElasticDal(es).insert_document('audio',{'name':'berale', 'age':'24'}, '44')

Test().insert_into_elastic('44',{'name':'berale', 'age':'24'})

#
#
#
#
#
#
#
#
#
#
#
