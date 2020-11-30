#!/usr/bin/env python3
'''
Redis basic
'''
import redis
import uuid
from typing import Union, Optional, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''
    Count the number of times a method is called
    '''
    key = method.__qualname__
    @wraps(method)
    def wrapper(self, *args, **kwds):
        '''
        Wrapper function
        '''
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    '''
    Cache class
    '''
    def __init__(self):
        '''
        Store an instance of Redis and flush it
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Store data using a random key
        '''
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        '''
        Convert data to the desired format
        '''
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)
