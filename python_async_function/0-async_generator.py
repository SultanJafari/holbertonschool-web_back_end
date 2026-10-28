#!/usr/bin/env python3
"""Module for AsyncGenerator coroutine tasks."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Wait for a random and 0-10."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
