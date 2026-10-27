#!/usr/bin/env python3
"""task of project measure_time."""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Run measure_time sum times."""
    start = time.time()
    wtask = asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time = end - start
    total_sum = total_time / n
    return total_sum
