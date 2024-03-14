#!/usr/bin/env python3
"""
function to Annotate  parameters and return values
with the appropriate types
"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    function to anotate parameter and return value
    args:
        lst: parameter
    Return: annotated values
    """
    return [(i, len(i)) for i in lst]
