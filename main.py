__author__ = 'guillermo'

from rdflib import Literal, Graph
from rdflib.namespace import RDF, RDFS
from rdf_utils.namespaces_handler import *
from generator import observations_generator as observations


def main():
    g = Graph()
    for obs in observations():
        g.add((no_prefix.term(obs.observation_id), RDF.type,
               qb.term("Observation")))
        g.add((no_prefix.term(obs.observation_id), cex.term("ref-time"),
               Literal(obs.ref_time)))
        g.add((no_prefix.term(obs.observation_id), cex.term("ref-indicator"),
               Literal(obs.indicator)))
        g.add((no_prefix.term(obs.observation_id), cex.term("value"),
               Literal(obs.value)))
        g.add((no_prefix.term(obs.observation_id), cex.term("computation"),
               cex.term(obs.computation)))
        g.add((no_prefix.term(obs.observation_id), dcterms.term("issued"),
               Literal(obs.issued)))
        g.add((no_prefix.term(obs.observation_id), RDFS.label,
               Literal(obs.description)))
        g.add((no_prefix.term(obs.observation_id),
               sdmx_concept.term("obsStatus"), cex.term(obs.computation)))
        g.add((no_prefix.term(obs.ref_area), RDF.type,
               no_prefix.term("Country")))
        g.add((no_prefix.term(obs.ref_time), RDF.type, no_prefix.term("Time")))
        #g.add((no_prefix.term(obs.indicator), RDF.type, cex.term("Indicator")))

    bind_namespaces(g)

    serialized = g.serialize(format='turtle')

    with open('generated/sample.ttl', 'w') as sample:
        sample.write(serialized)

    print serialized


if __name__ == "__main__":
    main()