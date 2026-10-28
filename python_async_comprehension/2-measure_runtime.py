#!/usr/bin/env python3
"""Async generator module andpython_async_comprehension."""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """task of  2-measure_runtime.py"""
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
        )
    end = time.time()
    total_time = end - start
    return total_time
