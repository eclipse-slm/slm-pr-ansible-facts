import unittest

from convert_v2 import convert_to_submodel


class UnitTests(unittest.TestCase):
    object = {
        'key1': 'value1',
        'key2': 1,
        'key3': 5.7,
        'key4': True
    }

    expected = {
        'length': len(object),
        "value_type": ["xs:string", "xs:integer", "xs:float", "xs:boolean"],
    }

    submodel = convert_to_submodel(object)
    submodel_elements = submodel['submodelElements']

    def test_count_of_submodel_elements(self):
        actual =  len(self.submodel_elements)
        expected = self.expected['length']

        # Check Count
        self.assertEqual(
            actual,
            expected,
            'Submodel Count does not match expected length'
        )

    def test_id_short_of_submodel_elements(self):
        for index, o in enumerate(self.object):
            actual = self.submodel_elements[index]['idShort']
            expected = o

            # Assert id short
            self.assertEqual(
                actual,
                expected,
                f'Submodel Element ID does not match expected value "{expected}"'
            )

    def test_value_type_of_submodel_elements(self):
        for index, o in enumerate(self.object):
            actual = self.submodel_elements[index]['valueType']
            expected = self.expected['value_type'][index]

            # Assert value_type
            self.assertEqual(
                actual,
                expected,
                f'Submodel Element Value Type does not match expected value "{expected}"'
            )

    def test_value_of_submodel_elements(self):
        for index, o in enumerate(self.object):
            actual = self.submodel_elements[index]['value']
            expected = str(self.object[o]).lower()

            # Assert value
            self.assertEqual(
                actual,
                expected,
                f'Submodel Element Value does not match expected value "{expected}"'
            )


if __name__ == '__main__':
    unittest.main()
