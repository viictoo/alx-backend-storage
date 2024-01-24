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
from functools import wraps

count = 0
cache = redis.Redis()


def url_count(method):
    """Decorator for get_page function"""
    @wraps(method)
    def wrapper(url):
        """Wrapper function"""
        cache.incr(f"count:{url}")
        key = cache.get(f"cached:{url}")
        if key:
            return key.decode("utf-8")
        resp = method(url)
        cache.setex(f"cached:{url}", 10, resp)
        return resp
    return wrapper


@url_count
def get_page(url: str) -> str:
    """obtain the resp content"""
    results = requests.get(url)
    return results.text
