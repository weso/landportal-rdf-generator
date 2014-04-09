__author__ = 'guillermo'

import requests
from requests.auth import HTTPDigestAuth

url = 'http://localhost:1300/sparql-graph-crud-auth?graph-uri=urn:graph:update:test1:post'

dataset = {'file': open('generated/dataset.rdf', 'rb')}

headers = {'content-type': 'text/html'}

r = requests.post(url, files=dataset, auth=HTTPDigestAuth('dba', 'root'),
                  headers=headers)

print r.status_code
print r.text
