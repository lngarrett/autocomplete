import json
products = json.load(open('products.json'))

from elasticsearch import Elasticsearch
es = Elasticsearch(
    ['elasticsearch'],
    scheme="http",
    port=9200,
)

counter = 0
for product in products:
    counter += 1
    try:
        res = es.index(
            index='products',
            doc_type='product',
            body=product,
            id=counter
        )
        print(product['name'])
    except:
        pass
