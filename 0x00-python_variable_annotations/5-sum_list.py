#!/usr/bin/env python3
"""This a function that sums a list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums list of floats
    Args:
        input_list (list): A list of floats
    Returns:
        float: Sum of the floats in the list
    """
    if input_list is None:
        return 0
    else:
        return sum(input_list)