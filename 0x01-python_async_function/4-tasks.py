#!/usr/bin/env python3
"""
coroutin function
"""
import asyncio
from typing import List


task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:

    """
    a routin to display or return a list of delay in
    ascending orde
    args:
        n:number of list item
        max_delay:max amount ofseconds function delayed
        Return: list of delay time in sorted order
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
