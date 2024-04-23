
#!/usr/bin/env python3
"""This  a python module to returns 10 random numbers using async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    async_comprehension-A function to return 10 random numbers
    Arguments:
        no arguments
    Returns:
        10 random numbers
    """
    rslt = [i async for i in async_generator()]
    return rslt

