#!/usr/bin/python3
for i in range(26, 0, -1):
    if(i % 2 != 0):
        c = i + 64
    else:
        c = i + 96
    print("{:s}".format(chr(c)), end='')
