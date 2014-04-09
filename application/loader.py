__author__ = 'guillermo'

import requests
from requests.auth import HTTPDigestAuth

url1 = "http://localhost:1300/sparql-graph-crud-auth?graph-uri=urn:graph:update:test1:post"
url2 = "http://localhost:1300/DAV/home/dba/rdf_sink/.rdf"

dataset = {'file': open('generated/dataset.rdf', 'rb')}

headers = {'content-type': 'text/html'}

r1 = requests.post(url1, files=dataset, auth=HTTPDigestAuth('dba', 'root'),
                   headers=headers)

r2 = requests.post(url2, files=dataset, auth=('dba', 'root'))

print "Request1: " + str(r1.status_code)
print r1.text
print "Request2: " + str(r2.status_code)
print r2.text
