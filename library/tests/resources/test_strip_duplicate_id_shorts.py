import json
import logging
import sys
import unittest

import basyx
from basyx.aas import model

from convert_v2 import strip_submodels_with_duplicate_id_short

logger = logging.getLogger()
logger.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)


class PropertySetElement(model.Property):
    def __key(self):
        return self.id_short

    def __hash__(self):
        return hash(self.__key())

    def __eq__(self, other):
        return self.__key() == other.__key()


class UnitTests(unittest.TestCase):
    id_short = 'id_short'
    value_type = basyx.aas.model.datatypes.String
    value = 'value'
    submodel_elements = set()

    for _ in range(3):
        submodel_element = PropertySetElement(
            value_type=value_type,
            value=str(_)
        )
        submodel_elements.add(submodel_element)

    def test_strip_duplicate_id_shorts(self):
        se_list = list(self.submodel_elements)

        for se in self.submodel_elements:
            print(se.value)

