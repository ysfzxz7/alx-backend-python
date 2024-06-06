#!/usr/bin/env pyhton3

"""
the sum list module
"""


def sum_list(input_list: list[float]) -> float:
    """
    func sum_list takes a list of float as arg
    return:
    the sum of the list
    """
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
