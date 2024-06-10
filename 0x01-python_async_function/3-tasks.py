#!/usr/bin/env python3
"""
    Module of tasks
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
        Function that returns a new task of the wait_random function
    """
    return asyncio.create_task(wait_random(max_delay))
