#!/usr/bin/python3
def no_c(my_string):
    str_list = []
    new_str = ""
    for i in range(len(my_string)):
        if(my_string[i] != 'c' and my_string[i] != 'C'):
            str_list.append(my_string[i])
    for c in str_list:
        new_str += c
    return new_str
