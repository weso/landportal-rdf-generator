__author__ = 'guillermo'

from rdflib import Namespace, URIRef

# Namespaces
empty = Namespace("http://example.org/")
cex = Namespace("http://purl.org/weso/computex/ontology#")
dcterms = Namespace("http://purl.org/dc/terms/")
qb = Namespace("http://purl.org/linked-data/cube#")
sdmx_concept = Namespace("http://purl.org/linked-data/sdmx/2009/concept#")

def bind_namespaces(graph):
    graph.namespace_manager.bind("", URIRef("http://example.org/"))
    graph.namespace_manager.bind("cex", URIRef("http://purl.org/weso/computex/ontology#"))
    graph.namespace_manager.bind("dcterms", URIRef("http://purl.org/dc/terms/"))
    graph.namespace_manager.bind("qb", URIRef("http://purl.org/linked-data/cube#"))
    graph.namespace_manager.bind("sdmx_concept", URIRef("http://purl.org/linked-data/sdmx/2009/concept#"))