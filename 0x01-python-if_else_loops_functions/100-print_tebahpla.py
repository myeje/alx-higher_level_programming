#!/usr/bin/python3
for j in range(122, 96, -1):
    if j % 2 == 0:
        print("{}".format(chr(j)), end='')
    else:
        print("{}".format(chr(j - 32)), end='')
