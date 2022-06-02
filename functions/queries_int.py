"""
 9 Agregar nuevo administrador con datos ficticios a "paddockManagers" y agregar un
  nuevo cuartel de tipo NOGALES con 900mts2, año 2017 de AGRICOLA SANTA ANA,
  administrado por este nuevo administrador
 Luego devolver el lugar que ocupa este nuevo administrador en el ranking de la pregunta 3.
 No modificar arreglos originales para no alterar las respuestas anteriores al correr la solución

"""

from .aux_functions import list_names_sort


def new_manager_ranking(paddock_managers, paddocks) -> int:
    new_paddock_managers = paddock_managers
    new_paddock_managers_user = {
        'id': 7, 'taxNumber': '302254524', 'name': 'ROSAMEL FIERRO DURO'}
    new_paddock_managers.append(new_paddock_managers_user)
    new_paddocks = paddocks
    new_paddocks.append({'paddockManagerId': 7, 'farmId': 1,
                         'paddockTypeId': 4, 'harvestYear': 2017, 'area': 900})

    list_names = list_names_sort('paddockManagerId', 'area', new_paddocks, new_paddock_managers)
    return list_names.index(new_paddock_managers_user['name'])
