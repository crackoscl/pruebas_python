from data.data import farms, paddock_managers, paddocks, paddock_type
from functions.queries_int import new_manager_ranking
from functions.queries_list import (list_paddock_manager_ids,
                                    list_paddock_managers_by_name,
                                    sort_paddock_type_by_total_area,
                                    sort_farm_manager_by_admin_area,
                                    biggest_avocado_farms,
                                    biggest_cherries_managers)
from functions.queries_dict import (farm_manager_names,
                                    farm_manager_paddocks,
                                    paddocks_type_managers, )


def main():
    print(list_paddock_manager_ids(paddock_managers))  # 0
    print(list_paddock_managers_by_name(paddock_managers))  # 1
    print(sort_paddock_type_by_total_area(paddock_type, paddocks))  # 2
    print(sort_farm_manager_by_admin_area(paddock_managers, paddocks))  # 3
    print(farm_manager_names(farms, paddocks, paddock_managers))  # 4
    print(biggest_avocado_farms(paddock_type, paddocks, farms))  # 5
    print(biggest_cherries_managers(farms, paddocks,
                                    paddock_managers, paddock_type))  # 6
    print(farm_manager_paddocks(farms, paddocks, paddock_managers))  # 7
    print(paddocks_type_managers(paddocks, paddock_managers, paddock_type))  # 8
    print(new_manager_ranking(paddock_managers, paddocks))  # 9


if __name__ == "__main__":
    main()
