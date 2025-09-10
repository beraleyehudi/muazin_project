from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')
my_index = 'test'
document = {'name':'berale', 'age':'24'}
# es.indices.delete(index=my_index)
# es.indices.create(index=my_index)
print(es.index(index='test', id='27', document=document))

res = es.search(index=my_index, body={'query':{'match_all':{}}})
for hit in res['hits']['hits']:
    print(f'source: {hit['_source']}')

print([doc['_source'] for doc in res['hits']['hits']])

def update_document(index, document_id, update_data):
    update_data = {'doc': update_data}
    try:
        response = es.update(index=index, id=document_id, body=update_data)
        print(f"Document updated successfully: {response['_id']}")
    except Exception as e:
        print(f"Error updating document: {e}")


update_document('test', '25',  {'text': 'this achla text yes yes'})
updated_doc = es.get(index=my_index, id='25')
print(f"Updated document: {updated_doc['_source']}")



