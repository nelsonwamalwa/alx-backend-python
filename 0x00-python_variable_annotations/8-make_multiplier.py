#!/usr/bin/env python3
"""A function that multiplies a float by multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float by multiplier
    Args:
        multiplier (float): Multiplier
    Returns:
        Function that multiplies a float by multiplier
    """

    def multiplier_func(number: float) -> float:
        """Multiplies a float by multiplier"""
        return multiplier * number

    return multiplier_func