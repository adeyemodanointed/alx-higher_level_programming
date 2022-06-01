#!/usr/bin/python3
def uppercase(str):
    strlen = len(str)
    for i in range(strlen):
        if(ord(str[i]) > 96 and ord(str[i]) < 123):
            c = chr(ord(str[i])-32)
        else:
            c = str[i]
        print("{}".format(c), end='')
    print("")
