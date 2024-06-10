#!/usr/bin/env python3
"""
    This is the Module of the waitRandom func
"""


import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """
    wait_random func take one opt parameter max_delay
        return the delay generated otherwise 10,
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
