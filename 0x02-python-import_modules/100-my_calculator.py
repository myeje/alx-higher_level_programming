#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    amount = len(sys.argv)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if amount != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] == '+':
        answer = add(a, b)
    elif sys.argv[2] == '-':
        answer = sub(a, b)
    elif sys.argv[2] == '*':
        answer = mul(a, b)
    elif sys.argv[2] == '/':
        answer = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, sys.argv[2], b, answer))
