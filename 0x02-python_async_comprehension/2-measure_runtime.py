#!/usr/bin/env python3
"""
    Module of measure_runtime
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        Function that measures the time of execution
    """
    start = time.time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    return time.time() - start
