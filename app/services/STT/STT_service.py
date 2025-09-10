from app.connections import MongoConnection, Consumer, Producer
from app.connections.elasticsearch import ElasticConnection
from app.dal import MongoDal
from app.dal.elastic_dal import ElasticDal
from app.services.STT.STT_helper import STTHelper


class STTService:
    def __init__(self):
        self._elastic_dal = ElasticDal(ElasticConnection())
        self._mongo_dal = MongoDal(MongoConnection())
        self._collection_name = 'audio'
        self._stt_helper = STTHelper()



    def load_sst(self):
        docs = self._mongo_dal.get_all_documents(self._collection_name)
        for doc in docs:
            stt = self._stt_helper.text_from_speach(doc.get('_id'), doc.get('data'))
            self._elastic_dal.update_document(self._collection_name, doc.get('_id'), {'text':stt})
