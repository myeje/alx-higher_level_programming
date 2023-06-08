#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = len(sys.argv) - 1

    if a == 0:
        print("0 arguments.")
    elif a == 1:
        print("1 argument:".format(sys.argv))
        for j in range(a):
            print("{}: {}".format(j + 1, sys.argv[j + 1]))
    else:
        print("{} arguments:".format(a))
        for j in range(a):
                print("{}: {}".format(j + 1, sys.argv[j + 1]))
