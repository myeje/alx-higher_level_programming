#!/usr/bin/python3
def uppercase(str):
    for j in str:
        index = ord(j)
        if index >= 97 and index <= 122:
            index = index - 32
        print("{:c}".format(index), end='')
    print()
