#!/usr/bin/env python3

"""
Module for the mixed list
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    this sum_mixed_list takes a list of mixed int float
    return:
    the sum as float
    """
    sum: float = 0
    for i in mxd_lst:
        sum += i
    return sum
