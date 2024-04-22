#!/usr/bin/env python3
"""
This includes a function that initiates the execution of
wait_random n times, with a set interval between each invocation.

"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Generate 'wait_random' function calls 'n' times with 
    a designated delay between each invocation. Parameters 
    include 'n' for the number of iterations and 'max_delay' 
    for the maximum duration between calls. The function 
    returns a list containing the delays.
    """
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]