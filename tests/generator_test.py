from unittest import TestCase

from application.models import Observation


__author__ = 'guillermo'


class GeneratorTest(TestCase):

    def setUp(self):
        self.generated_obs_id = Observation("some_string", 10)

    def test_observation_id_generation(self):
        self.assertEquals(self.generated_obs_id.observation_id, "OBSSOME_STRING10")



