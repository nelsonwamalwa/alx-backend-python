#!/usr/bin/env python3
"""
This module measures the execution time of an asynchronous comprehension.
"""

import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    measure_runtime - Executes async_comprehension 4 times and measures the total execution time.
    
    Returns:
        The total execution time required to complete the task.
    """
    t_start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    t_end = time.perf_counter()
    return t_end - t_start

