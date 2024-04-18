#!/usr/bin/env python3
"""
A function that returns  a list of integers
multiplied by certain factor.
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """A list of integers multiplied by certain factor.
    Args:
        lst: Turple of integers.
        factor: An integer.
    Returns:
        List of integers.
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array: Tuple = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)