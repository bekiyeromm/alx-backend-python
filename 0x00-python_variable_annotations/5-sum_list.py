#!/usr/bin/env python3
"""
function sum_list which takes a list input_list of floats as
argument and returns their sum as a float.
"""
from typing import List


def sum_list(input_list: list[float]) -> float:
    """
    calculate the sum of float in a list
    """
    """
    an other way of finding sum
    sum: float = 0.0
    for list_item in input_list:
        sum += list_item
    return flost(sum)
    """
    return float(sum(input_list))
