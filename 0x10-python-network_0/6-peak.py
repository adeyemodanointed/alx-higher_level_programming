#!/usr/bin/python3
"""contains the function find_peak"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    li = list(set(list_of_integers))
    lo = len(li)
    if lo == 0:
        return
    return li[lo-1]
