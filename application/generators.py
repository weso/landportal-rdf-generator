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
            for ind in xrange(rand_num)]


def generate_slices():
    datasets = generate_datasets()
    indicators = generate_indicators()
    return [Slice(chain_for_id="", int_for_id=slc, dimension="Area",
                  dataset=datasets[slc].dataset_id,
                  indicator=indicators[slc].name_en)
            for slc in xrange(rand_num)]


def generate_regions():
    return [Region("Region" + str(region)) for region in xrange(rand_num)]


def generate_countries():
    regions = generate_regions()
    return [Country("Country" + str(country), regions[country].name,
                    "co", "cou") for country in xrange(rand_num)]


def generate_years():
    return [Year(name="year" + str(rand_year), value=rand_year)
            for year in xrange(rand_num)]


computation = Computation("RAW")


def generate_datasources():
    return [DataSource("dataSource", src, "dataSource"
                       + str(src)) for src in xrange(rand_num)]


def generate_datasets():
    datasources = generate_datasources()
    return [Dataset("", dat, "freq-A", "license" + str(dat),
                    datasources[dat].name) for dat in xrange(rand_num)]


def generate_observations():
    """
    Generates a random number of observations based on fake data
    for testing purposes
    """
    years = generate_years()
    indicators = generate_indicators()
    datasets = generate_datasets()
    regions = generate_regions()
    slices = generate_slices()

    return [Observation(chain_for_id="", int_for_id=obs,
                        ref_time=years[obs].name,
                        issued=dt.datetime.now(),
                        computation=computation.uri,
                        value=float(obs),
                        indicator=indicators[obs].name_en,
                        dataset=datasets[obs].dataset_id,
                        ref_area=regions[obs].name,
                        description="Observation of "
                        + regions[obs].name + " in " +
                        years[obs].name + " for " +
                        indicators[obs].name_en, source="upload"
                        + str(obs), status="obsStatus-A",
                        slice=slices[obs])
            for obs in xrange(rand_num)]


def generate_topics():
    return [Topic(topic="Topic" + str(topic)) for topic in xrange(rand_num)]


def generate_measurements():
    return [MeasurementUnit(name="measurement" + str(measure))
            for measure in xrange(rand_num)]


def generate_uploads():
    observations = generate_observations()
    datasources = generate_datasources()

    return [Upload(name="upload" + str(upload), user="user" + str(upload),
            timestamp=dt.datetime.now(),
            ip="156.34.56." + str(upload),
            observations=observations[upload].observation_id,
            datasource=datasources[upload].name)
            for upload in xrange(rand_num)]


def generate_organizations():
    return [Organization(str(org), name="organization" + str(org),
                         url="<http://www." + "organization" + str(org)
                         + ".org/>", description="Description of " +
                         "organization" + str(org))
            for org in xrange(rand_num)]


def generate_licenses():
    return [License(name="license" + str(lic)) for lic in xrange(rand_num)]


def generate_users():
    organizations = generate_organizations()
    return [User(user_login=str(usr),
            organization=organizations[usr].name) for usr in xrange(rand_num)]

