#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    delete_keys = []
    for keys in a_dictionary:
        if a_dictionary[keys] == value:
            delete_keys.append(keys)
    for keys in delete_keys:
        del a_dictionary[keys]
    return(a_dictionary)
