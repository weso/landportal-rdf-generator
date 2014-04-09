__author__ = 'guillermo'

from SPARQLWrapper import SPARQLWrapper, TURTLE

endpoint = "http://localhost:1300/sparql"
graph = "http://local.virt/DAV/home/dba/rdf_sink/dataset.ttl"

sparql = SPARQLWrapper(endpoint,
                       defaultGraph=graph)
sparql.setQuery("""
    select distinct ?Concept where {[] a ?Concept} LIMIT 100
""")
sparql.setReturnFormat(TURTLE)
results = sparql.query()

for result in results:
    print result