def list_names_sort(str_1, str_2, dict_1, dict_2) -> list:
    new_data = {}
    for elem in dict_1:
        elem_id = elem[str_1]
        value = elem[str_2]
        new_data[elem_id] = new_data.get(elem_id, 0) + value
    data = [{''.join([d['name'] for d in dict_2 if d['id'] == key]): value}
            for key, value in new_data.items()]
    sorted_ = sorted(data, key=lambda x: list(x.values()), reverse=True)
    return [i for s in [d.keys() for d in sorted_] for i in s]


def dict_names_sort(paddock_manager_id, farm_id, v_append, farms, paddocks, paddock_managers) -> dict:
    paddock_managers_dict = {pd['id']: pd for pd in paddock_managers}
    farms_dict = {f['id']: f for f in farms}
    dict_sorted = {}
    if v_append != 'name':
        new_paddocks = sorted(
            paddocks, key=lambda x: paddock_managers_dict[x[paddock_manager_id]]['name'])
        for p in new_paddocks:
            pm = paddock_managers_dict[p[paddock_manager_id]]
            f = farms_dict[p[farm_id]]
            key = f['name']
            if key not in dict_sorted:
                dict_sorted[key] = []
            if pm[v_append] in dict_sorted[key]:
                continue
            dict_sorted[key].append(pm[v_append])
    else:
        new_paddocks = sorted(
            paddocks, key=lambda f: farms_dict[f[farm_id]]['name'])
        for p in new_paddocks:
            pm = paddock_managers_dict[p[paddock_manager_id]]
            fm = farms_dict[p[farm_id]]
            key = pm['name']
            if key not in dict_sorted:
                dict_sorted[key] = []
            if fm[v_append] in dict_sorted[key]:
                continue
            dict_sorted[key].append(fm[v_append])
    return dict_sorted
