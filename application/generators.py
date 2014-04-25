__author__ = 'guillermo'

from random import randint
import datetime as dt

from application.models import *


rand_num = 10
rand_year = randint(1999, 2014)


def generate_indicators():

    return [Indicator("test_indicator", ind, "Indicator"
                      + str(ind), description_en="Indicator" + str(ind)
                      + " description", preferable_tendency="decrease",
                      measurement_unit="measurement" + str(ind),
                      last_update=dt.datetime.now(), starred=True,
                      topic="topic" + str(ind), indicator_type="Simple")
            for ind in range(rand_num)]


def generate_slices():
    return [Slice(chain_for_id="", int_for_id=slc, dimension="Area",
                  dataset=generate_datasets()[slc],
                  indicator=generate_indicators()[slc]) for slc in range(rand_num)]


def generate_regions():
    return [Region("Region" + str(region)) for region in range(rand_num)]


def generate_countries():
    return [Country("Country" + str(country), generate_regions()[country],
                    "co", "cou") for country in range(rand_num)]


def generate_years():
    return [Year("year" + str(rand_year), rand_year) for year in range(rand_num)]


computations = []

def generate_computations():
    computations.append(Computation("RAW"))
    return computations


def generate_datasources():
    return [DataSource("dataSource", src, "dataSource"
                       + str(src)) for src in range(rand_num)]


def generate_datasets():
    return [Dataset("", dat, "freq-A", "license" + str(dat),
                    generate_datasources()[dat]) for dat in range(rand_num)]


def generate_observations():
    """
    Generates a random number of observations based on fake data
    for testing purposes
    """
    return [Observation("", obs, generate_years()[obs],
                        dt.datetime.now(),
                        generate_computations()[obs],
                        float(obs),
                        generate_indicators()[obs],
                        generate_datasets()[obs],
                        str(generate_regions()[obs]),
                        "Observation of "
                        + str(generate_regions()[obs]) + " in " +
                        str(generate_years()[obs]) + " for " +
                        str(generate_indicators()[obs]), "upload"
                        + str(obs), "obsStatus-A",
                        generate_slices()[obs])
            for obs in range(rand_num)]


def generate_topics():
    return [Topic(topic="Topic" + str(topic)) for topic in range(rand_num)]


def generate_measurements():
    return [MeasurementUnit(name="measurement" + str(measure))
            for measure in range(rand_num)]


def generate_uploads():
    return [Upload(name="upload" + str(upload), user="user" + str(upload),
            timestamp=dt.datetime.now(),
            ip="156.34.56." + str(upload),
            observations=generate_observations()[:2],
            datasource=generate_datasources()[upload])
            for upload in range(rand_num)]


def generate_organizations():
    return [Organization(str(org), name="organization" + str(org),
                         url="<http://www." + "organization" + str(org)
                         + ".org/>", description="Description of " +
                         "organization" + str(org))
            for org in range(rand_num)]


def generate_licenses():
    return [License(name="license" + str(lic)) for lic in range(rand_num)]


def generate_users():
    return [User(user_login=str(usr),
            organization=generate_organizations()[usr]) for usr in range(rand_num)]

