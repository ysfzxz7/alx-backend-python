#!/usr/bin/env python3
"""
    Module of measure_runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        Function that returns an average execution time of many coroutines
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))

    return (time.time() - start_time) / n
