#!/usr/bin/env python3
"""
function sum_mixed_list which takes a list mxd_lst of integers and
floats and returns their sum as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    function that calculates the sum of mixed list
    args:
        mxd_list: a list of int and float type
    Return: return float value of sum
    """
    return float(sum(mxd_lst))
