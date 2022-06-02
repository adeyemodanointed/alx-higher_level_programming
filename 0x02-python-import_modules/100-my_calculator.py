#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    argv_l = len(argv)
    if argv_l != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        quit(1)
    else:
        a = int(argv[1])
        op = argv[2]
        b = int(argv[3])
        if op == "+":
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif op == "-":
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        elif op == "*":
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        elif op == "/":
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            quit(1)
