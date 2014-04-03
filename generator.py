__author__ = 'guillermo'

from models import *
from random import randint
import pprint


num_regions = randint(1, 10)
num_indicators = randint(1, 10)
num_years = randint(1, 10)

regions = []
indicators = []
observations = []


def observations_generator():
    counter = 0
    for region in range(num_regions):
        for indicator in range(num_indicators):
            for year in range(num_years):
                indicators.append(Indicator("test_indicator" + str(counter),
                                            float(counter),
                                            "Indicator" + str(counter)))
                regions.append(Region("Region"))

                observations.append(Observation("_test_observation",
                                                counter, "Year2013", 2013, "Raw",
                                                float(counter), indicators[indicator], None,
                                                str(regions[region]) + str(counter),
                                                "Observation of " + str(regions[region])
                                                + str(counter)))
                counter += 1
    return observations



