#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv_l = len(argv)
    if (argv_l == 1):
        print("{:d} arguments.".format(argv_l-1))
    elif(argv_l == 2):
        print("{:d} argument:\n{:d}: {}".format(argv_l-1, argv_l-1, argv[1]))
    else:
        print("{:d} arguments:".format(argv_l-1))
        for i in range(1, argv_l):
            print("{:d}: {}".format(i, argv[i]))
