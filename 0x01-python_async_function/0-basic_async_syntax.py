#!/usr/bin/env python3
"Contains a coroutine that pauses for a specified duration before returning."

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
This function generates a random decimal number
within the range of 0 to the specified maximum delay.

Parameters:

max_delay: The upper limit for the delay time.
Returns:
A randomly generated decimal number within 
the range of 0 to max_delay.
    """
    rand = random.uniform(0, max_delay)
    await asyncio.sleep(rand)
    return rand
