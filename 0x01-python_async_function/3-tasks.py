#!/usr/bin/env python3
"""
a function to return asyncio.Task
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    a function which takes one argument max_delay
    and returns asyncio.Task
    args:
        max_delay: the maximun delay time
    """
    coroutin = wait_random(max_delay)
    task = asyncio.ensure_future(coroutin)
    return task
