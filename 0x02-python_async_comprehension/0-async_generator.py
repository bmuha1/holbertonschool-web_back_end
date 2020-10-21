#!/usr/bin/env python3
'''
Wait for a second then yield a random number between 0 and 10, 10 times
'''
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''
    Wait for a second then yield a random number between 0 and 10, 10 times
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
