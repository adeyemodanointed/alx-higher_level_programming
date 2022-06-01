#!/usr/bin/python3
for i in range(9):
    for j in range(10):
        if(j > i):
            print("{:d}".format(i), end = '')
            if(j == 9 and i == 8):
                print("{:d}".format(j))
                continue
            print("{:d}".format(j), end = ', ')
