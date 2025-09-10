from app.connections.elasticsearch import ElasticConnection
from app.dal.elastic_dal import ElasticDal
from app.services.text_classification.text_classification_helper import TextClassificationHelper


class TextClassificationService:
    def __init__(self):
        self._elastic_dal = ElasticDal(ElasticConnection.get_connection())
        self._index_name = 'audio'
        self._helper = TextClassificationHelper()



    def add_risk_field(self, doc_id, score):
        is_bds = self._helper.is_risk(score)
        self._elastic_dal.update_document(self._index_name, doc_id, is_bds)

    def add_classification_field(self, doc_id, score):
        classification = self._helper.classification_by_category(score)
        self._elastic_dal.update_document(self._index_name, doc_id, classification)

    def get_service(self):
        for doc in self._elastic_dal.get_all_document(self._index_name):
            score = self._helper.calculate_text_classification(doc['text'])
            self.add_risk_field(doc.get('_id'), score)
            self.add_classification_field(doc.get('_id'), score)
