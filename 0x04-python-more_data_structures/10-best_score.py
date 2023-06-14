#!/usr/bin/python3
#def best_score(a_dictionary):
#    return (max(a_dictionary, key=a_dictionary.get) if a_dictionary else None)

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    keys_max = None
    values_max = float('-inf')

    for keys, values in a_dictionary.items():
        if values > values_max:
            keys_max = keys
            values_max = values
    return (keys_max)
