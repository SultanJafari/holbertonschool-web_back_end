#!/usr/bin/env python3
"""Async generator module andpython_async_comprehension."""

import asyncio
import random
from typing import List


async_generator = __import__('0-async_generator').async_generator

async def async_comprehension()->List[float]:
    """task of 1-async_comprehension.py"""
    return [n async for n in async_generator()]
