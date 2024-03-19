#!/usr/bin/env python3
'''
Calculates run time of 4 parallel co-routines
'''

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Calculates the total runtime of 4 async-comprehension

    Args: N/A

    Return: The total time taken for 4 parallel runs of async comprehension
    '''
    start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    """await asyncio.gather(*(async_comprehension() for i in range(4)))"""
    return time.time() - start_time
