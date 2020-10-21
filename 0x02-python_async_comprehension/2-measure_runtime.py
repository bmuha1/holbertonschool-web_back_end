#!/usr/bin/env python3
'''
Measure the total runtime for executing async_comprehension four times in
parallel using asynio.gather
'''
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure the total runtime for executing async_comprehension four times in
    parallel using asynio.gather
    '''
    s = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.perf_counter() - s
