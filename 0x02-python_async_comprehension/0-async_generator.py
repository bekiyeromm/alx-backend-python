#!/usr/bin/env python3
"""
coroutin async_generator that takes no arguments
"""
import asyncio
import random


async def async_generator():
    """
    coroutin async_generator that takes no arguments
    which will loop 10 times, each time asynchronously wait 1 second
    Return:random number between 0 and 10
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
