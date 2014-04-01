__author__ = 'guillermo'

from models import Observation, Indicator
from rdflib import Literal, Graph
from rdflib.namespace import RDF, RDFS
from random import randint
from generator import *


def main():
    num_counties = randint(10, 50)
    num_indicators = randint(10, 50)
    num_years = randint(20, 30)
    g = Graph()
    total_triples = 0

    for country_num in range(num_counties):
        for indicator_num in range(num_indicators):
            for year_num in range(num_years):
                pass

                total_triples += 1

    ind = Indicator("test_indicator", 9, "hdi")
    obs = Observation("test_observation", 3, "year2013", 2013, "Raw", 2.3, ind.name_en)

    g.add((empty.term(obs.observation_id), RDF.type, qb.term("Observation")))
    g.add((empty.term(obs.observation_id), cex.term("ref-time"), Literal(obs.ref_time)))
    g.add((empty.term(obs.observation_id), cex.term("ref-indicator"), Literal(obs.indicator)))
    g.add((empty.term(obs.observation_id), cex.term("value"), Literal(obs.value)))
    g.add((empty.term(obs.observation_id), cex.term("computation"), cex.term(obs.computation)))
    g.add((empty.term(obs.observation_id), dcterms.term("issued"), Literal(obs.issued)))
    g.add((empty.term(obs.observation_id), RDFS.label, Literal("Observation of Spain in 2013")))
    g.add((empty.term(obs.observation_id), sdmx_concept.term("obsStatus"), cex.term(obs.computation)))

    bind_namespaces(g)

    with open('generated/sample.ttl', 'w') as sample:
        sample.write(g.serialize(format='turtle'))

    print total_triples


if __name__ == "__main__":
     main()