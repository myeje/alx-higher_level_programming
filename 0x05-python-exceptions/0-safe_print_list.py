#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        amount = 0
        for i in range(x):
            print("{}".format(my_list[i]), end="")
            amount += 1
        print()
        return (amount)
    except Exception:
        print()
        return (amount)
