import unittest

from convert_v2 import convert_to_submodel


class UnitTests(unittest.TestCase):
    object_elements = {
        'key1': 'value1',
        'key2': 1,
        'key3': 5.7,
        'key4': True,
        'key5': ["1", "2", "3"],
        'key6': {
            'key_1_1': "1",
            'key_1_2': "2",
            'key_1_3': "3"
        },
    }
    object_list = {
        'list1': ["1", "2", "3"],
        'list2': [1, 2, 3],
        'list3': [1.3, 2.5, 3.1],
        'list4': [True, False, False],
    }
    object_collection = {
        'collection1': {
            'key1': "1",
            'key2': "2",
            'key3': "3"
        },
        'collection2': {
            'key1': 1,
            'key2': 2,
            'key3': 3
        },
        'collection3': {
            'key1': 1.4,
            'key2': 2.7,
            'key3': 3.1
        },
        'collection4': {
            'key1': True,
            'key2': False,
            'key3': False
        }
    }

    submodel = convert_to_submodel(object_collection)
    submodel_elements = submodel['submodelElements']

    print(object_elements)
    print(submodel)

    # def test_count_of_submodel_elements(self):
    #     actual =  len(self.submodel_elements)
    #     expected = self.expected['length']
    #
    #     # Check Count
    #     self.assertEqual(
    #         actual,
    #         expected,
    #         'Submodel Count does not match expected length'
    #     )
    #
    # def test_id_short_of_submodel_elements(self):
    #     for index, o in enumerate(self.object):
    #         actual = self.submodel_elements[index]['idShort']
    #         expected = o
    #
    #         # Assert id short
    #         self.assertEqual(
    #             actual,
    #             expected,
    #             f'Submodel Element ID does not match expected value "{expected}"'
    #         )
    #
    # def test_value_type_of_submodel_elements(self):
    #     for index, o in enumerate(self.object):
    #         actual = self.submodel_elements[index]['valueType']
    #         expected = self.expected['value_type'][index]
    #
    #         # Assert value_type
    #         self.assertEqual(
    #             actual,
    #             expected,
    #             f'Submodel Element Value Type does not match expected value "{expected}"'
    #         )
    #
    # def test_value_of_submodel_elements(self):
    #     for index, o in enumerate(self.object):
    #         actual = self.submodel_elements[index]['value']
    #         expected = str(self.object[o]).lower()
    #
    #         # Assert value
    #         self.assertEqual(
    #             actual,
    #             expected,
    #             f'Submodel Element Value does not match expected value "{expected}"'
    #         )


if __name__ == '__main__':
    unittest.main()
