#!/usr/bin/env python3
'''
Return a tuple containing the start and end indexes
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    '''
    Return a tuple containing the start and end indexes
    '''
    return (page * page_size - page_size, page * page_size)
