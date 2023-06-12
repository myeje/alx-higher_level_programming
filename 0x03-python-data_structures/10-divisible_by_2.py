#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    bool_list = []
    for j in my_list:
        if j % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)
    return (bool_list)
