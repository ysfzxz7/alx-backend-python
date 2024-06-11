#!/usr/bin/env python3
"""
    Module of async_comprehension
"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
        Function that returns 10 random floating numbers
    """
    res = [i async for i in async_generator()]
    return res
