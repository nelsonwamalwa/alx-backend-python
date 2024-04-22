#!/usr/bin/env python3
"This contains a function that starts the execution of wait_random n times, with a defined interval between each call."
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
   """Generate calls to the 'wait_random' function 'n' times, 
   with a specified delay between each call. Parameters include 
   'n' for the number of iterations and 'max_delay' for the 
   maximum duration between calls. The function returns a list 
   containing the delays."""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await task for task in asyncio.as_completed(tasks)]