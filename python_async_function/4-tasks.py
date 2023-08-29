#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 4-task
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Take the code from wait_n and alter it into a new function task_wait_n. The
    code is nearly identical to wait_n except task_wait_random is being called.
-------------------------------------------------------------------------------
IMPORTS:
-------------------------------------------------------------------------------
    asyncio: to use the Coroutine that completes after a given time(in seconds)
-------------------------------------------------------------------------------
'''
import asyncio
from typing import List


get = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return a list of task"""
    list_task = [get(max_delay) for i in range(n)]
    finish = [await task for task in asyncio.as_completed(list_task)]
    return finish
