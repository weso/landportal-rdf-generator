__author__ = 'guillermo'

from random import randint
import datetime as dt

from application.models import *


rand_num = randint(5, 10)
rand_year = randint(1999, 2014)


def generate_indicators():
    indicators = []
    for ind in range(rand_num):
        indicators.append(Indicator("test_indicator", ind, "Indicator"
                          + str(ind)))
    return indicators


def generate_slices():
    slices = []
    for slc in range(rand_num):
        slices.append(Slice("", slc, "Area", generate_datasets()[slc],
                            generate_indicators()[slc]))
    return slices


def generate_regions():
    regions = []
    for region in range(rand_num):
        regions.append(Region("Region" + str(region)))
    return regions


def generate_countries():
    countries = []
    for country in range(rand_num):
        countries.append(Country("Country" + str(country), generate_regions()[country],
                         "co", "cou"))
    return countries


def generate_years():
    years = []
    for year in range(rand_num):
        years.append(Year("year" + str(rand_year), rand_year))
    return years


computations = []


def generate_computations():
    computations.append(Computation("RAW"))
    return computations


def generate_datasources():
    datasources = []
    for src in range(rand_num):
        datasources.append(DataSource("dataSource", src, "dataSource"
                                      + str(src)))
    return datasources


def generate_datasets():
    datasets = []
    for dat in range(rand_num):
        datasets.append(Dataset("", dat, "freq-A", "license" + str(dat),
                                generate_datasources()[dat]))
    return datasets


def generate_observations():
    """
    Generates a random number of observations based on fake data
    for testing purposes
    """
    observations = []
    for obs in range(rand_num):
                observations.append(Observation("", obs, generate_years()[obs],
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
                                                generate_slices()[obs]))
    return observations

