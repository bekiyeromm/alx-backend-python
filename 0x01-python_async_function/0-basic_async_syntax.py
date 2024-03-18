#!/usr/bin/env python3
"""
coroutin function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """
    a coroutin function which generates a delay betwen the given
    range
    arg:
        max_delay: the maximum delay time
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(max_delay)
    return delay
