__author__ = 'guillermo'

import requests

url = 'http://localhost:1300/sparql-graph-crud-auth?graph-uri=urn:graph:update:test:post'

files = {'file': open('generated/dataset.rdf', 'rb')}

r = requests.post(url, files=files, auth=('dba', 'root'))

print r.status_code
print r.content
print r.text
