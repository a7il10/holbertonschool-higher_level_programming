#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if el == search else el for el in my_list]





    new_list = []
    for idx in my_list:
        if el == search:
            new_list.append(replace)
        else:
            new_list.append(el)
    return new_list