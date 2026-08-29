#!/usr/bin/env python3
"""Measure runtime of async comprehensions."""

import asyncio
import time

async_comprehension = __import__(
    '1-async_comprehension'
).async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime for four async comprehensions."""
    start = time.time()

    await asyncio.gather(
        *(async_comprehension() for _ in range(4))
    )

    return time.time() - start
