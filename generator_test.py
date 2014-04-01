from unittest import TestCase
from models import Observation

__author__ = 'guillermo'


class ObservationTest(TestCase):

    def setUp(self):
        self.output = Observation("some_string", 10)

    def test_observation_generation(self):
        self.assertEquals(self.output.observation_id, "OBSSOME_STRING10")



