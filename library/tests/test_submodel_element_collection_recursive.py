import unittest

from convert import convert_to_submodel

unittest.TestLoader.sortTestMethodsUsing = None


class UnitTests(unittest.TestCase):
    object = {
        'collection1': {
            'collection2': {
                'collection3': {
                    'collection4': {
                        'key1': "value1"
                    }
                }
            }
        }
    }

    object_2 = {
        'collection_1': {
            'collection_2': {
                'key_3_1': 'value_3_1',
            },
            'key_2_1': 'value_2_1',
            'key_2_2': 'value_2_2'
        },
        'key_1_1': 'value_1_1'
    }

    submodel = convert_to_submodel(object)
    submodel_elements = submodel['submodelElements']
    submodel_elements_length = len(submodel_elements)

    expected = {
        'length': len(object),
        'model_type': 'SubmodelElementCollection',
        'id_short': list(object.keys())[0],
        'type_value': 'Property',
        'collections': {
            'collection1': {
                'length_list': len(object['collection1']),
                'value_type': 'xs:string'
            },
            'collection2': {
                'length_list': len(object['collection2']),
                'value_type': 'xs:integer'
            },
            'collection3': {
                'length_list': len(object['collection3']),
                'value_type': 'xs:float'
            },
            'collection4': {
                'length_list': len(object['collection4']),
                'value_type': 'xs:boolean'
            },
        }
    }

    print(object)
    print(submodel)


if __name__ == '__main__':
    unittest.main()
