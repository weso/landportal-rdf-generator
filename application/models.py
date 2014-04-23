__author__ = 'guillermo'


class Observation(object):
    def __init__(self, chain_for_id, int_for_id, ref_time=None, issued=None,
                 computation=None, value=None, indicator=None, dataset=None,
                 ref_area = None, description=None, source=None, status=None, slice=None):
        self.ref_time = ref_time
        self.issued = issued
        self.computation = computation
        self.value = value
        self.indicator = indicator
        self.dataset = dataset
        self.group = None
        self.indicator_group = None
        self.source = source
        self.status = status
        self.slice = slice
        self.description = description
        self.ref_area = ref_area

        self.observation_id = self._generate_id(chain_for_id, int_for_id)

    @staticmethod
    def _generate_id(chain_for_id, int_for_id):
        return "OBS" + chain_for_id.upper() + str(int_for_id).upper()

    def __repr__(self):
        return "Observation=> " + "RefTime: " + self.ref_time + \
               " Indicator: " + str(self.indicator) + " Computation: " + \
               str(self.computation) + " Issued: " + str(self.issued) + \
               " Value: " + str(self.value) + " RefArea: " + str(self.ref_area)\
               + " Description: " + str(self.description) + "Source" + str(self.source) \
               + "Status" + str(self.status)


class Indicator(object):
    TOPIC_CLIMATE_CHANGE = "TOP1"
    TOPIC_COUNTRY_DATA = "TOP2"
    TOPIC_FOOD_SEC_AND_HUNGER = "TOP3"
    TOPIC_LAND_AND_GENDER = "TOP4"
    TOPIC_LAND_TENURE = "TOP5"
    TOPIC_SOCIO_ECONOMIC_AND_POVERTY = "TOP6"
    TOPIC_USAGE_AND_INVESTMENT = "TOP7"
    TOPIC_TEMPORAL = "TOP99"

    def __init__(self, chain_for_id, int_for_id, name_en=None, name_es=None,
                 name_fr=None, description_en=None, description_es=None,
                 description_fr=None, dataset=None, measurement_unit=None,
                 topic=None):
        self.name_en = name_en
        self.name_es = name_es
        self.name_fr = name_fr
        self.description_en = description_en
        self.description_es = description_es
        self.description_fr = description_fr
        self.dataset = dataset
        self.measurement_unit = measurement_unit
        self.topic = topic

        self.indicator_id = self._generate_id(chain_for_id, int_for_id)

    @staticmethod
    def _generate_id(chain_for_id, int_for_id):
        return "IND" + chain_for_id.upper() + str(int_for_id).upper()

    def __repr__(self):
        return self.name_en


from abc import ABCMeta, abstractmethod


class Dimension(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_dimension_string(self): pass


class Region(Dimension):
    def __init__(self, name=None, is_part_of=None):
        self.name = name
        self.is_part_of = is_part_of
        self.observations = []

    def add_observation(self, observation):
        self.observations.append(observation)
        observation.region = self

    def get_dimension_string(self):
        return self.name

    def __repr__(self):
        return self.name


class Country(Region):
    def __init__(self, name=None, is_part_of=None, iso2=None, iso3=None):
        super(Country, self).__init__(name, is_part_of)
        self.iso2 = iso2
        self.iso3 = iso3

    def get_dimension_string(self):
        return self.iso3


class Year(object):
    def __init__(self, year=None):
        self.year = year


class Topic(object):
    def __init__(self, topic=None):
        self.topic = topic


class MeasurementUnit(object):
    def __init__(self, name=None):
        self.name = name


class Slice(object):
    def __init__(self, chain_for_id, int_for_id, dimension=None, dataset=None, indicator=None):
        self.dataset = dataset
        self.indicator = indicator
        self.dimension = dimension
        self.observations = []
        self.slice_id = self._generate_id(chain_for_id, int_for_id)

    def __repr__(self):
        return self.slice_id

    @staticmethod
    def _generate_id(chain_for_id, int_for_id):
        return "SLI" + chain_for_id.upper() + str(int_for_id).upper()

    def add_observation(self, observation):
        self.observations.append(observation)
        observation.data_slice = self


class Dataset(object):
    def __init__(self, chain_for_id, int_for_id, frequency=None,
                 license_type=None, source=None):
        self.frequency = frequency
        self.license_type = license_type
        self.source = source
        self.slices = []
        self.observations = []
        self.indicators = []
        self.dataset_id = self._generate_id(chain_for_id, int_for_id)

    @staticmethod
    def _generate_id(chain_for_id, int_for_id):
        return "DAT" + chain_for_id.upper() + "_" + str(int_for_id).upper()

    def add_slice(self, data_slice):
        self.slices.append(data_slice)
        data_slice.dataset = self

    def add_observation(self, observation):
        self.observations.append(observation)
        observation.dataset = self

    def add_indicator(self, indicator):
        self.indicators.append(indicator)
        indicator.dataset = self

    def __repr__(self):
        return self.dataset_id


class DataSource(object):
    def __init__(self, chain_for_id=None, int_for_id=None, name=None, organization=None):
        self.name = name
        self.organization = organization
        self.datasets = []
        self.source_id = self._generate_id(chain_for_id, int_for_id)

    @staticmethod
    def _generate_id(chain_for_id, int_for_id):
        return "SOU" + chain_for_id.upper() + str(int_for_id).upper()

    def add_dataset(self, dataset):
        self.datasets.append(dataset)
        dataset.source = self


class Organization(object):
    def __init__(self, chain_for_id, name=None, url=None, description=None, url_logo=None, is_part_of=None):
        self.name = name
        self.url = url
        self.is_part_of = is_part_of
        self.description = description
        self.url_logo = url_logo
        self.data_sources = []
        self.users = []
        self.organization_id = self._generate_id(chain_for_id)

    @staticmethod
    def _generate_id(chain_for_id):
        return "ORG" + chain_for_id.upper()

    def add_user(self, user):
        self.users.append(user)
        user.organization = self

    def add_data_source(self, data_source):
        self.data_sources.append(data_source)
        data_source.organization = self


class License(object):
    def __init__(self, name=None, description=None, republish=None, url=None):
        self.name = name
        self.description = description
        self.republish = republish
        self.url = url


class Computation(object):
    def __init__(self, uri=None):
        self.uri = uri

    def __repr__(self):
        return self.uri


class User(object):
    def __init__(self, user_login, organization=None):
        self.organization = organization
        self.user_id = self._generate_id(user_login)

    @staticmethod
    def _generate_id(user_login):
        return "USR" + user_login.upper()


