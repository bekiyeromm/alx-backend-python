#!/usr/bin/env python3
'''
a rootin to return list of random numbers
'''

import typing

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    '''
    Produces a list of 10 random numbers
    Return: List of 10 random numbers
    '''
    return [random_num async for random_num in async_generator()]
