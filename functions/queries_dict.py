from .aux_functions import dict_names_sort

"""
4 objeto en que las claves sean los nombres de los campos y los valores un arreglo
con los ruts de sus administradores ordenados alfabéticamente por nombre.
"""


def farm_manager_names(farms, paddocks, paddock_managers) -> dict:
    return dict_names_sort('paddockManagerId', 'farmId', 'taxNumber', farms, paddocks, paddock_managers)


"""
7 Objeto en el cual las claves sean el nombre del administrador y el valor un arreglo con los
nombres de los campos que administra, ordenados alfabéticamente

"""


def farm_manager_paddocks(farms, paddocks, paddock_managers) -> dict:
    return dict_names_sort('paddockManagerId', 'farmId', 'name', farms, paddocks, paddock_managers)


"""
8 Objeto en que las claves sean el tipo de cultivo concatenado con su año de plantación
(la concatenación tiene un separador de guión ‘-’, por ejemplo AVELLANOS-2020)
 y el valor otro objeto en el cual la clave sea el id del administrador y el valor el nombre del administrador

"""


def paddocks_type_managers(paddocks, paddock_managers, paddock_type) -> dict:
    paddock_managers_dict = {pd['id']: pd for pd in paddock_managers}
    paddock_type_dict = {pd['id']: pd for pd in paddock_type}
    data = {}
    for p in paddocks:
        pt = paddock_type_dict[p['paddockTypeId']]
        pm = paddock_managers_dict[p['paddockManagerId']]
        key_pm_id = pm['id']
        value_pm_name = pm['name']
        pt_name = pt['name']
        pt_year = p['harvestYear']
        key = f'{pt_name}-{pt_year}'
        if key not in data:
            data[key] = {key_pm_id: value_pm_name}
        else:
            data[key].update({key_pm_id: value_pm_name})
    return data
