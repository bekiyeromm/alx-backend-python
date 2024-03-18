#!/usr/bin/env python3
"""
a function to measure the total elapsed time
"""
import time
import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total execution time for wait_n(n, max_delay),
    args:
        n: number of list item
         max_delay: maximum delay time
    Returns: total_time / n. Your function should return a float.

    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return (total_time / n)
