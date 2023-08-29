#!/usr/bin/env python3
'''
-------------------------------------------------------------------------------
MODULE NAME : 3-task
-------------------------------------------------------------------------------
MODULE DESCRIPTION:
-------------------------------------------------------------------------------
    Write a function (do not create an async function, use the regular function
    syntax to do this) task_wait_random that takes an integer max_delay and ret
    urns a asyncio.Task.
-------------------------------------------------------------------------------
IMPORTS:
-------------------------------------------------------------------------------
    asyncio: to use the Coroutine that completes after a given time(in seconds)
-------------------------------------------------------------------------------
'''
import asyncio
from asyncio import Task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """return a task"""
    loop = asyncio.get_event_loop()
    task = loop.create_task(wait_random(max_delay))
    return task
