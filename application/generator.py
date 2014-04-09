__author__ = 'guillermo'

from random import randint
import datetime as dt

from application.models import *


num_regions = randint(5, 10)
num_indicators = randint(5, 10)
num_years = randint(5, 10)

regions = []
indicators = []
observations = []


def observations_generator():
    """
    Generates a random number of observations based on fake data
    for testing purposes
    """
    counter = 0
    for region in range(num_regions):
        for indicator in range(num_indicators):
            for year in range(num_years):
                indicators.append(Indicator("test_indicator" + str(counter),
                                            float(counter),
                                            "Indicator" + str(counter)))
                regions.append(Region("Region"))

                observations.append(Observation("_test_observation_",
                                                counter, "Year" +
                                                dt.datetime.now().
                                                strftime("%Y"),
                                                dt.datetime.now(),
                                                "Raw", float(counter),
                                                indicators[counter], None,
                                                str(regions[region]) +
                                                str(counter), "Observation of "
                                                + str(regions[region]) +
                                                str(counter) + " in " +
                                                "Year" + dt.datetime.now().
                                                strftime("%Y") + " for " +
                                                str(indicators[counter])
                                                ))
                counter += 1
    return observations