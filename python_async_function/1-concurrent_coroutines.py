#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 1-concurrent_coroutines
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Import wait_random from the previous python file that you've written and wr
    ite an async routine called wait_n that takes in 2 int arguments (in this o
    rder): n and max_delay. You will spawn wait_random n times with the specifi
    ed max_delay.

    wait_n should return the list of all the delays (float values). The list of
    the delays should be in ascending order without using sort() because of con
    currency.
-------------------------------------------------------------------------------
IMPORTS:
-------------------------------------------------------------------------------
    asyncio: to use the Coroutine that completes after a given time(in seconds)
    wait_random: that funcion return a random time sync
-------------------------------------------------------------------------------
'''
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of dalays"""
    list_delay = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    list_delay_finish = [await delay for delay in asyncio.as_completed(list_delay)]
    return list_delay_finish
