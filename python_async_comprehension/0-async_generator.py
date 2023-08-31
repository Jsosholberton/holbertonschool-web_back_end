#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 0-async_generator
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Write a coroutine called async_generator that takes no arguments.

    The coroutine will loop 10 times, each time asynchronously wait 1 second, t
    hen yield a random number between 0 and 10. Use the random module.
-------------------------------------------------------------------------------
IMPORTS:
-------------------------------------------------------------------------------
    asyncio: to use the Coroutine that completes after a given time(in seconds)
-------------------------------------------------------------------------------
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loop 10 times, asynchronously"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
