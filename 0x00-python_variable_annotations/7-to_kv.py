#!/usr/bin/env python3
"""
a  function taht takes two different types of values
and returns a tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    function that returns a tuple
    args:
        k: string input
        v: int or float input
    Return:tuple
    """
    return (k, float(v ** 2))
