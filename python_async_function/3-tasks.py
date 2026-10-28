#!/usr/bin/env python3
"""task of project wait_random andtask_wait_random ."""

import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """create_task of max delay."""
    task = wait_random(max_delay)
    ctask = asyncio.create_task(task)
    return ctask
