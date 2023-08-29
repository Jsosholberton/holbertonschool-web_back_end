#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 0-basic_async_syntax
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Write an asynchronous coroutine that takes in an integer argument (max_dela
    y, with a default value of 10) named wait_random that waits for a random de
    lay between 0 and max_delay (included and float value) seconds and eventual
    ly returns it.
-------------------------------------------------------------------------------
IMPORTS:
-------------------------------------------------------------------------------
    asyncio: to use the Coroutine that completes after a given time(in seconds)
    random: to generate a ramdom number in this case from 0 to 10(pred.)
-------------------------------------------------------------------------------
'''
import asyncio
import random


async def wait_random(max_delay=10):
    delay  = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
