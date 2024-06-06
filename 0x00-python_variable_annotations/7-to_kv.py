#!/usr/bin/env python3

"""
Module to the to_kv func
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int | float]) -> Tuple:
    """
    func to_kv that takes k and v as parms
    return:
    a tuple of the given values
    """
    my_t: tuple = (k, v)
    return my_t
