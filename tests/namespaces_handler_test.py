from unittest import TestCase
from rdf_utils.namespaces_handler import *

__author__ = 'guillermo'


class NamespacesTest(TestCase):

    def setUp(self):
        self.empty_prefix = no_prefix
        self.cex_prefix = cex
        self.dcterms_prefix = dcterms
        self.qb_prefix = qb
        self.sdmx_concept_prefix = sdmx_concept

    def test_empty_prefix(self):
        self.assertEquals(self.empty_prefix, "http://example.org/")

    def test_cex_prefix(self):
        self.assertEquals(self.cex_prefix, "http://purl.org/weso/computex/ontology#")

    def test_dctermns_prefix(self):
        self.assertEquals(self.dcterms_prefix, "http://purl.org/dc/terms/")

    def test_qb_prefix(self):
        self.assertEquals(self.qb_prefix, "http://purl.org/linked-data/cube#")

    def test_sdmx_concept_prefix(self):
        self.assertEquals(self.sdmx_concept_prefix, "http://purl.org/linked-data/sdmx/2009/concept#")

    def test_namespace_binding(self):
        pass

