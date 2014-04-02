__author__ = 'guillermo'

from models import *
from random import randint
from math import pow

random_num = int(pow(randint(1, 100), 2))

regions = []
indicators = []
observations = []


def observations_generator():
    for n in range(random_num):
        indicators.append(Indicator("test_indicator" + str(n), float(n),
                                    "Indicator" + str(n)))
        regions.append(Region("Region"))

        observations.append(Observation("test_observation" + str(n),
                                        n, "year2013", 2013, "Raw",
                                        float(n), indicators[n], None,
                                        str(regions[n]) + str(n),
                                        "Observation of " + str(regions[n])
                                        + str(n)))
    return observations





