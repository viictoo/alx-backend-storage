#!/usr/bin/env python3
""" implements a get_page function (prototype: def get_page(url: str) -> str:)
    The core of the function is very simple. It uses the requests module to
    obtain the HTML content of a particular URL and returns it.

    get_page tracks how many times a particular URL was accessed in the key
    "count:{url}" and cache the result with an expiration time of 10 seconds.

    Bonus: implement this use case with decorators.
"""
import redis
import requests
from typing import Callable
from functools import lru_cache


count = 0
cache = redis.Redis()

def trackUrl(method: Callable) -> Callable:
    @lru_cache(maxsize=100)
    def wrapper(url):
        # resp = requests.get(url)
        # body = resp.text
        # count[url] = count.get(url, 0) + 1
        # return body
        cache.incr(f'count:{url}')
        key = cache.get(f'key:{url}')
        if key:
            return key.decode('utf-8')
        key = method(url)
        cache.set(f'count:{url}', 0)
        cache.setex(f'key:{url}', 10, key)
        return key
    return wrapper


@trackUrl
def get_page(url: str) -> str:
    return requests.get(url).text
