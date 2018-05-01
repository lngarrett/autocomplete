import json
products = json.load(open('products.json'))

from elasticsearch import Elasticsearch
es = Elasticsearch(
    ['elasticsearch'],
    scheme="http",
    port=9200,
)

for product in products:
    try:
        res = es.index(
            index='products',
            doc_type='product',
            body=product
        )
        print(product['name'])
    except:
        pass
