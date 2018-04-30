# things.py

# Let's get this party started!
import falcon
import json

from elasticsearch import Elasticsearch
es = Elasticsearch(
    ['es'],
    scheme="http",
    port=9200,
)

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class SearchResource(object):
    def on_get(self, req, resp):
        query = req.get_param('query')
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  # This is the default status

        search = {
            "query": {
                "match": {
                    "name": {
                        "query":    query,
                        "analyzer": "standard"
                    }
                }
            }
        }

        res = es.search(
            index="products",
            doc_type='product',
            _source=True,
            body=search)
        suggestions = []
        for suggestion in res['hits']['hits']:
            item = {'name': suggestion['_source']['name']}
            suggestions.append(item)
        print(suggestions)
        resp.body = (json.dumps(suggestions))

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
search = SearchResource()

# things will handle all requests to the '/things' URL path
app.add_route('/search', search)
