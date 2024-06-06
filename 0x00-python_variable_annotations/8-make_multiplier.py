#!/usr/bin/env python3

"""
This is the Module of the make fun
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make_mul get x float
    return:
    a fun func
    """
    def fun(y: float) -> float:
        return multiplier * y
    return fun
