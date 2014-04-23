__author__ = 'guillermo'

from random import randint
import datetime as dt

from application.models import *

regions = []
indicators = []
computations = []
datasets = []
datasources = []
slices = []
observations = []

rand_num = randint(5, 10)


def regions_generator():
    counter = 0
    for region in range(rand_num):
        regions.append(Region("Region" + str(counter)))
        counter += 1
    return regions


def observations_generator():
    """
    Generates a random number of observations based on fake data
    for testing purposes
    """
    counter = 0
    for rand1 in range(rand_num):
        #for rand2 in range(randint(5, 10)):
            #for rand3 in range(randint(5, 10)):
                indicators.append(Indicator("test_indicator",
                                            counter, "Indicator" + str(counter)))
                regions_generator()

                computations.append(Computation("RAW"))

                datasources.append(DataSource("dataSource", counter, "dataSource"
                                   + str(counter)))

                datasets.append(Dataset("", counter, "freq-A",
                                        "license" + str(counter), datasources[counter]))

                slices.append(Slice("", counter, "Area", datasets[counter],
                                    indicators[counter]))

                observations.append(Observation("", counter, "Year" +
                                                dt.datetime.now(). strftime("%Y"),
                                                dt.datetime.now(), computations[counter],
                                                float(counter), indicators[counter],
                                                datasets[counter],
                                                str(regions[rand1]) +
                                                str(counter), "Observation of "
                                                + str(regions[rand1]) + " in " +
                                                "Year" + dt.datetime.now().
                                                strftime("%Y") + " for " +
                                                str(indicators[counter]), "upload" +
                                                str(counter), "obsStatus-A",
                                                slices[counter]))
                counter += 1
    return observations

