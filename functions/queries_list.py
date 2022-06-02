
from .aux_functions import  list_names_sort
# 0 Arreglo con los ids de los responsables de cada cuartel

def list_paddock_manager_ids(paddock_managers) -> list:
    return [manager_id['id'] for manager_id in paddock_managers]

# 1 Arreglo con los ruts de los responsables de los cuarteles, ordenados por nombre

def list_paddock_managers_by_name(paddock_managers) -> list:
    return [manager_rut['taxNumber'] for manager_rut  in (sorted(paddock_managers,key=lambda name:name['name']))]

# 2 Arreglo con los nombres de cada tipo de cultivo, ordenados decrecientemente por la suma TOTAL
# de la cantidad de hectáreas plantadas de cada uno de ellos.

def sort_paddock_type_by_total_area(paddock_type, paddocks) -> list:
    return list_names_sort('paddockTypeId','area',paddocks,paddock_type)

# 3 Arreglo con los nombres de los administradores, ordenados decrecientemente
# por la suma TOTAL de hectáreas que administran.
def sort_farm_manager_by_admin_area(paddock_managers, paddocks) -> list:
    return list_names_sort('paddockManagerId', 'area', paddocks,paddock_managers)

# 5 Arreglo ordenado decrecientemente con los m2 totales de cada campo que
# tengan más de 2 hectáreas en Paltos

def biggest_avocado_farms(paddock_type, paddocks, farms) -> list:
    id_avocado = [x['id'] for x in paddock_type if x['name'] == 'PALTOS']
    list_dict_avocados = [
        x for x in paddocks if x['paddockTypeId'] == id_avocado[0]]
    new_data = {}
    for elem in list_dict_avocados:
        elemid = elem["farmId"]
        value = elem["area"]
        new_data[elemid] = new_data.get(elemid, 0) + value
    return sorted([x for x in new_data.values() if x > 20000], reverse=True)

# 6 Arreglo con nombres de los administradores de la FORESTAL Y AGRÍCOLA LO ENCINA,
# ordenados por nombre, que trabajen más de 1000 m2 de Cerezas
def biggest_cherries_managers(farms, paddock, paddock_managers, paddock_type) -> list:
    farm_id = [x['id']
               for x in farms if x['name'] == 'FORESTAL Y AGRICOLA LO ENCINA']
    paddock_ty = [x['id'] for x in paddock_type if x['name'] == 'CEREZAS']
    paddockManagerId_ = [x['paddockManagerId'] for x in paddock if x['farmId']
                         == farm_id[0] and x['area'] > 1000 and x['paddockTypeId'] == paddock_ty[0]]
    return [pn['name'] for pn in paddock_managers if pn['id'] == paddockManagerId_[0]]
