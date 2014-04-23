__author__ = 'guillermo'

from rdflib import Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS

from rdf_utils.namespaces_handler import *
from application.generator import observations_generator
from application.generator import regions_generator
from application.loader import load_data_set

g = Graph()
host1 = "http://localhost:1300/"
api1 = "sparql-graph-crud-auth?"
graph_uri1 = "graph-uri=http://www.landportal.info"


def initialize_graph_with_regions():
    for region in regions_generator():
        g.add((prefix_.term(region), RDF.type,
               cex.term("Area")))


def initialize_graph_with_observations():
    for obs in observations_generator():
        g.add((prefix_.term(obs.observation_id), RDF.type,
               qb.term("Observation")))

        g.add((prefix_.term(obs.observation_id), cex.term("ref-time"),
               prefix_.term(obs.ref_time)))

        g.add((prefix_.term(obs.observation_id), cex.term("ref-area"),
               prefix_.term(obs.ref_area)))

        g.add((prefix_.term(obs.observation_id), cex.term("ref-indicator"),
               prefix_.term(str(obs.indicator))))

        g.add((prefix_.term(obs.observation_id), cex.term("value"),
               Literal(obs.value, datatype=XSD.double)))

        g.add((prefix_.term(obs.observation_id), cex.term("computation"),
               cex.term(str(obs.computation))))

        g.add((prefix_.term(obs.observation_id), dcterms.term("issued"),
               Literal(obs.issued, datatype=XSD.dateTime)))

        g.add((prefix_.term(obs.observation_id), qb.term("dataSet"),
               prefix_.term(str(obs.dataset))))

        g.add((prefix_.term(obs.observation_id), qb.term("slice"),
               prefix_.term(str(obs.slice))))

        g.add((prefix_.term(obs.observation_id), RDFS.label,
               Literal(obs.description, lang='en')))

        g.add((prefix_.term(obs.observation_id),
               sdmx_concept.term("obsStatus"), sdmx_code.term(obs.status)))

        g.add((prefix_.term(obs.observation_id),
               lb.term("source"), prefix_.term(obs.source)))

        g.add((prefix_.term(obs.ref_area), RDF.type,
               prefix_.term("Country")))

        g.add((prefix_.term(obs.ref_time), RDF.type, prefix_.term("Time")))

        g.add((prefix_.term(Literal(obs.indicator)), RDF.type,
               cex.term("Indicator")))


def initialize_graph():
    initialize_graph_with_regions()
    initialize_graph_with_observations()
    bind_namespaces(g)
    return g


def serialize_rdf_xml():
    serialized = initialize_graph().serialize(format='application/rdf+xml')
    with open('../generated/dataset.rdf', 'w') as sample:
        sample.write(serialized)


def serialize_turtle():
    serialized = initialize_graph().serialize(format='turtle')
    with open('../generated/dataset.ttl', 'w') as sample:
        sample.write(serialized)


def main():
    initialize_graph()
    serialize_rdf_xml()
    serialize_turtle()
    load_data_set(host1, api1, graph_uri1)

if __name__ == "__main__":
    main()