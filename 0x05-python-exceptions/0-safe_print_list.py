#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    if (x == 0):
        return
    for val in range(x):
        try:
            print("{:d}".format(my_list[val]), end="")
            count += 1
        except IndexError:
            break
    print()
    return count
