import json

import basyx
from basyx.aas import model
from basyx.aas.adapter.json import AASToJsonEncoder

submodel = model.Submodel('id')


def process_dict_element(key, value):
    dict_elements = []

    for v in value:
        if isinstance(value[v], dict):
            p_e = process_dict_element(v, value[v])
            if p_e is not None:
                # dict_elements[key] = p_e
                dict_elements.append(p_e)
            # (dict_elements.append(p_e) if p_e is not None else dict_elements)
        elif isinstance(value[v], list):
            pass
        else:
            # continue
            p_e = process_prim_element(v, value[v])
            if p_e is not None:
                # dict_elements[key] = p_e
                dict_elements.append(p_e)
            # (dict_elements.append(p_e) if p_e is not None else dict_elements)

    print(dict_elements)

    # if len(dict_elements) > 0:
    try:
        smc = model.SubmodelElementCollection(
            id_short=key,
            value=dict_elements
        )
    except AttributeError as e:
        smc = model.SubmodelElementCollection(
            id_short=key,
            value={}
        )
        print(e)
    # else:
    #     smc = model.SubmodelElementCollection(
    #         id_short=key,
    #         value=[]
    #     )

    return smc


def process_list_element(key, value):
    list_elements = []

    for index, v in enumerate(value):
        if isinstance(v, dict):
            continue
        elif isinstance(v, list):
            continue
        else:
            list_elements.append(
                process_prim_element(None, v)
            )

    if len(list_elements) > 0:
        smel = model.SubmodelElementList(
            id_short=key,
            value=list_elements,
            type_value_list_element=type(list_elements[0]),
            value_type_list_element=list_elements[0].value_type
        )
    else:
        smel = model.SubmodelElementList(
            id_short=key,
            value=[],
            type_value_list_element=model.SubmodelElement
        )

    return smel


def process_prim_element(key, value):
    try:
        if isinstance(value, bool):
            value_type = basyx.aas.model.datatypes.Boolean
            se_value = value
        elif isinstance(value, int):
            value_type = basyx.aas.model.datatypes.Integer
            se_value = value
        elif isinstance(value, float):
            value_type = basyx.aas.model.datatypes.Float
            se_value = value
        else:
            value_type = basyx.aas.model.datatypes.String
            se_value = str(value)

        return model.Property(
            id_short=key,
            value_type=value_type,
            value=se_value
        )
    except basyx.aas.model.base.AASConstraintViolation as e:
        print(e)


def process_element(key, value):
    if isinstance(value, dict):
        submodel.submodel_element.add(
            process_dict_element(key, value)
        )
    elif isinstance(value, list):
        submodel.submodel_element.add(
            process_list_element(key, value)
        )
    else:
        try:
            submodel.submodel_element.add(process_prim_element(key, value))
        except AttributeError as e:
            print(e)


def convert_to_submodel(object):
    submodel.id = 'https://ipa.fraunhofer.de/slm-pr-ansible-facts/test/submodel'

    for x in object:
        process_element(key=x, value=object[x])

    # with open('result.json', 'w') as f:
    #     f.write(json.dumps(submodel, cls=basyx.aas.adapter.json.AASToJsonEncoder, indent=2))

    return json.loads(
        json.dumps(submodel, cls=AASToJsonEncoder)
    )
