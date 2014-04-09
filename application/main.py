__author__ = 'guillermo'

from rdflib import Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS

from rdf_utils.namespaces_handler import *
from application.generator import observations_generator as observations


g = Graph()


def initialize_graph():
    for obs in observations():
        g.add((prefix_.term(obs.observation_id), RDF.type,
               qb.term("Observation")))

        g.add((prefix_.term(obs.observation_id), cex.term("ref-time"),
               prefix_.term(obs.ref_time)))

        g.add((prefix_.term(obs.observation_id), cex.term("ref-area"),
               prefix_.term(obs.ref_area)))

        g.add((prefix_.term(obs.observation_id), cex.term("ref-indicator"),
               prefix_.term(str(obs.indicator))))

        g.add((prefix_.term(obs.observation_id), cex.term("value"),
               Literal(obs.value, datatype=XSD.decimal)))

        g.add((prefix_.term(obs.observation_id), cex.term("computation"),
               cex.term(obs.computation)))

        g.add((prefix_.term(obs.observation_id), dcterms.term("issued"),
               Literal(obs.issued, datatype=XSD.dateTime)))

        g.add((prefix_.term(obs.observation_id), RDFS.label,
               Literal(obs.description, lang='en')))

        g.add((prefix_.term(obs.observation_id),
               sdmx_concept.term("obsStatus"), cex.term(obs.computation)))

        g.add((prefix_.term(obs.ref_area), RDF.type,
               prefix_.term("Country")))

        g.add((prefix_.term(obs.ref_time), RDF.type, prefix_.term("Time")))

        g.add((prefix_.term(Literal(obs.indicator)), RDF.type,
               cex.term("Indicator")))

    bind_namespaces(g)
    return g


def serialize_rdf_xml():
    serialized = initialize_graph().serialize(format='application/rdf+xml')
    with open('generated/../generated/dataset.rdf', 'w') as sample:
        sample.write(serialized)


def serialize_turtle():
    serialized = initialize_graph().serialize(format='turtle')
    with open('generated/../generated/dataset.ttl', 'w') as sample:
        sample.write(serialized)


def main():
    initialize_graph()
    serialize_rdf_xml()
    serialize_turtle()

if __name__ == "__main__":
    main()