#!/usr/bin/env python3
"""
coroutin function
"""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    a routin to display or return a list of delay in
    ascending orde
    args:
        n:number oflist item
        max_delay:max amount ofseconds function delayed
        Return: list of delay time in sorted order
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)
    return sorted(results)
