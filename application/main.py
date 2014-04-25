__author__ = 'guillermo'

from rdflib import Literal, Graph, XSD
from rdflib.namespace import RDF, RDFS, FOAF

from rdf_utils.namespaces_handler import *
from application.generators import generate_observations as observations
from application.generators import generate_regions as regions
from application.generators import generate_countries as countries
from application.generators import generate_years as years
from application.generators import generate_indicators as indicators
from application.generators import generate_topics as topics
from application.generators import generate_organizations as organizations
from application.generators import generate_licenses as licenses
from application.generators import generate_users as users
from application.generators import generate_measurements as measurements
from application.loader import load_data_set

g = Graph()
host1 = "http://localhost:1300/"
api1 = "sparql-graph-crud-auth?"
graph_uri1 = "graph-uri=http://www.landportal.info"


def add_regions_triples():
    for region in regions():
        g.add((prefix_.term(region.name), RDF.type,
               cex.term("Area")))

        g.add((prefix_.term(region.name), RDFS.label,
              Literal(region.name, lang='en')))

        g.add((prefix_.term(region.name), lb.term("UNCode"),
               Literal("EU")))


def add_countries_triples():
    for country in countries():
        g.add((prefix_.term(country.name), RDF.type,
               cex.term("Area")))
        g.add((prefix_.term(country.name), RDFS.label,
              Literal(country.name, lang='en')))
        g.add((prefix_.term(country.name), lb.term("FaoURI"),
               Literal("<http://www.fao.org/countryprofiles/index/en/?iso3=" +
                       country.iso3 + ">")))
        g.add((prefix_.term(country.name), lb.term("iso2"),
               Literal(str(country.iso2).upper())))
        g.add((prefix_.term(country.name), lb.term("iso3"),
               Literal(str(country.iso3).upper())))
        g.add((prefix_.term(country.name), lb.term("is_part_of"),
               prefix_.term(str(country.is_part_of))))


def add_years_triples():
    for year in years():
        g.add((prefix_.term(year.name), RDF.type,
               cex.term("Time")))
        g.add((prefix_.term(year.name), time.term("year"),
               Literal(year.value, datatype=XSD.gYear)))


def add_indicators_triples():
    for ind in indicators():
        g.add((prefix_.term(ind.name_en), RDF.type,
               cex.term("Indicator")))

        g.add((prefix_.term(ind.name_en), lb.term("preferable_tendency"),
               cex.term(ind.preferable_tendency)))

        g.add((prefix_.term(ind.name_en), lb.term("measurement"),
               cex.term(ind.measurement_unit)))

        g.add((prefix_.term(ind.name_en), lb.term("last_update"),
               Literal(ind.last_update, datatype=XSD.dateTime)))

        g.add((prefix_.term(ind.name_en), lb.term("starred"),
               Literal(ind.starred, datatype=XSD.Boolean)))

        g.add((prefix_.term(ind.name_en), lb.term("topic"),
               cex.term(ind.topic)))

        g.add((prefix_.term(ind.name_en), lb.term("indicatorType"),
               cex.term(ind.indicator_type)))

        g.add((prefix_.term(ind.name_en), RDFS.label,
               Literal(ind.description_en, lang='en')))

        g.add((prefix_.term(ind.name_en), RDFS.comment,
              Literal("Longer description of " + ind.name_en, lang='en')))


def add_observations_triples():
    for obs in observations():
        g.add((prefix_.term(obs.observation_id), RDF.type,
               qb.term("Observation")))

        g.add((prefix_.term(obs.observation_id), cex.term("ref-time"),
               prefix_.term(str(obs.ref_time))))

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
               cex.term("Area")))


def add_topics_triples():
    for topic in topics():
        g.add((prefix_.term(topic.topic), RDF.type,
               lb.term("Topic")))
        g.add((prefix_.term(topic.topic), RDFS.label,
               Literal(topic.topic, lang='en')))


def add_measurements_triples():
    for measure in measurements():
        g.add((prefix_.term(measure.name), RDF.type,
               lb.term("Measurement")))
        g.add((prefix_.term(measure.name), RDFS.label,
               Literal(measure.name, lang='en')))


def add_organizations_triples():
    for organization in organizations():
        g.add((prefix_.term(organization.name), RDF.type,
               org.term("Organization")))
        g.add((prefix_.term(organization.name), RDFS.label,
               Literal(organization.name, lang='en')))
        g.add((prefix_.term(organization.name), FOAF.homepage,
               Literal(organization.url)))


def add_licenses_triples():
    for lic in licenses():
        g.add((prefix_.term(lic.name), RDF.type,
               lb.term("License")))


def add_users_triples():
    for usr in users():
        g.add((prefix_.term(usr.user_id), RDF.type,
               FOAF.Person))
        g.add((prefix_.term(usr.user_id), RDFS.label,
               Literal(usr.user_id, lang='en')))
        g.add((prefix_.term(usr.user_id), FOAF.name,
               Literal(usr.user_id)))
        g.add((prefix_.term(usr.user_id), FOAF.account,
               Literal(usr.user_id)))
        g.add((prefix_.term(usr.user_id), org.term("memberOf"),
               prefix_.term(str(usr.organization))))


def initialize_graph():
    add_regions_triples()
    add_observations_triples()
    add_countries_triples()
    add_years_triples()
    add_indicators_triples()
    add_topics_triples()
    add_measurements_triples()
    add_organizations_triples()
    add_licenses_triples()
    add_users_triples()
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