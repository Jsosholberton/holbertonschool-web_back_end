#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 2-measure_runtime
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Import async_comprehension from the previous file and write a measure_runti
    me coroutine that will execute async_comprehension four times in parallel u
    sing asyncio.gather.

    measure_runtime should measure the total runtime and return it.

    Notice that the total runtime is roughly 10 seconds, explain it to yourself
-------------------------------------------------------------------------------
IMPORTS:
-------------------------------------------------------------------------------
    asyncio: to use the Coroutine that completes after a given time(in seconds)
-------------------------------------------------------------------------------
'''
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return a list of floats"""
    start_time = asyncio.get_event_loop().time()

    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = asyncio.get_event_loop().time()

    return end_time - start_time
