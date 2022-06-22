#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for val in range(list_length):
        try:
            new_val = my_list_1[val]/my_list_2[val]
        except ZeroDivisionError:
            print("division by 0")
            new_val = 0
        except TypeError:
            print("wrong type")
            new_val = 0
        except IndexError:
            print("out of range")
            new_val = 0
        finally:
            new_list.append(new_val)
    return new_list
