#!/usr/bin/env python3
'''
Take a string and an int or float and return a tuple containing the string
and the square of the int or float
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Take a string and an int or float and return a tuple containing the string
    and the square of the int or float
    '''
    return (k, v**2)
