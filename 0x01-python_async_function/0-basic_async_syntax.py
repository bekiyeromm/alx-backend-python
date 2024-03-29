#!/usr/bin/env python3
"""
coroutin function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    a coroutin function which generates a delay betwen the given
    range
    arg:
        max_delay: the maximum delay time
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
