#!/usr/bin/env python3
"""A function with annotated parameters and
returning values with appropriate types."""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returning list of tuples with the length of each element"""
    return [(i, len(i)) for i in lst]