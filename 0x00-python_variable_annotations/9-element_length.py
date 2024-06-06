#!/usr/bin/env python3

"""
The module of the func
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    a elem len take a lst as parm
    return:
    the lenght
    """
    return [(i, len(i)) for i in lst]
