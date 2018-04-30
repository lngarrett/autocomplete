import json
products = json.load(open('products.json'))

from elasticsearch import Elasticsearch
es = Elasticsearch(
    ['localhost'],
    scheme="http",
    port=9200,
)

for product in products:
    print(product['name'])
    res = es.index(
        index='products',
        doc_type='product',
        body=product
    )
