__author__ = 'guillermo'

from rdflib import Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS
from rdf_utils.namespaces_handler import *
from generator import observations_generator as observations

g = Graph()


def initialize_graph():
    for obs in observations():
        g.add((no_prefix.term(obs.observation_id), RDF.type,
               qb.term("Observation")))

        g.add((no_prefix.term(obs.observation_id), cex.term("ref-time"),
               Literal(obs.ref_time)))

        g.add((no_prefix.term(obs.observation_id), cex.term("ref-area"),
               Literal(obs.ref_area)))

        g.add((no_prefix.term(obs.observation_id), cex.term("ref-indicator"),
               no_prefix.term(str(obs.indicator))))

        g.add((no_prefix.term(obs.observation_id), cex.term("value"),
               Literal(str(obs.value))))

        g.add((no_prefix.term(obs.observation_id), cex.term("computation"),
               cex.term(obs.computation)))

        g.add((no_prefix.term(obs.observation_id), dcterms.term("issued"),
               Literal(obs.issued, datatype=XSD.dateTime)))

        g.add((no_prefix.term(obs.observation_id), RDFS.label,
               Literal(obs.description, lang='en')))

        g.add((no_prefix.term(obs.observation_id),
               sdmx_concept.term("obsStatus"), cex.term(obs.computation)))

        g.add((no_prefix.term(obs.ref_area), RDF.type,
               no_prefix.term("Country")))

        g.add((no_prefix.term(obs.ref_time), RDF.type, no_prefix.term("Time")))

        g.add((no_prefix.term(Literal(obs.indicator)), RDF.type,
               cex.term("Indicator")))

    bind_namespaces(g)
    return g


def serialize_rdf_xml():
    serialized = initialize_graph().serialize(format='application/rdf+xml')
    with open('generated/dataset.xml', 'w') as sample:
        sample.write(serialized)


def serialize_turtle():
    serialized = initialize_graph().serialize(format='turtle')
    with open('generated/dataset.ttl', 'w') as sample:
        sample.write(serialized)


def main():
    initialize_graph()
    serialize_rdf_xml()
    serialize_turtle()

if __name__ == "__main__":
    main()