#!/usr/bin/env python3

"""
    this is the concurrent module
"""

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    wait_n is a func that take two argss N and Max_Delay
        return a list of delays
    """
    croutines = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*croutines)
    return sorted(delays)
