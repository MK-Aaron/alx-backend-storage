#!/usr/bin/env python3
import redis
import uuid
from typing import Union
"""
Redis class caching
"""


class Cache:
    def __init__(self) -> None:
        sef._resis = redis.Redis()
        self.redis.flushdb()

    def store(self, daa: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
