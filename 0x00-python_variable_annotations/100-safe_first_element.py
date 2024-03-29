#!/usr/bin/env python3
"""
code with the correct duck-typed annotations
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    function to return the correct code annotation
    args:
        lst: argument
    Return: correct annotation for the given code
    """
    if lst:
        return lst[0]
    else:
        return None
