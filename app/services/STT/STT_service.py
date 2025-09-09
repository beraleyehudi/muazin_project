from app.connections import MongoConnection
from app.connections.elasticsearch import ElasticConnection
from app.dal import MongoDal
from app.dal.elastic_dal import ElasticDal
from app.services.STT.STT_helper import SSTHelper


class SSTService:
    def __init__(self):
        self._elastic_dal = ElasticDal(ElasticConnection.get_connection())
        self._mongo_dal = MongoDal(MongoConnection())
        self._collection_name = ''
        self._sst_helper = SSTHelper()

    def update_elastic_document(self, doc_id, text):
        pass

    def load_sst(self):
        docs = self._mongo_dal.get_all_documents(self._collection_name)
        for doc in docs:
            sst = self._sst_helper.text_from_speach(doc.get('data'))
            self.update_elastic_document(doc.get('_id'), sst)