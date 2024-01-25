#!/usr/bin/env python3
""" implements a get_page function (prototype: def get_page(url: str) -> str:)
    The core of the function is very simple. It uses the requests module to
    obtain the HTML content of a particular URL and returns it.

    get_page tracks how many times a particular URL was accessed in the key
    "count:{url}" and cache the respult with an expiration time of 10 seconds.

    Bonus: implement this use case with decorators.
"""
import redis
import requests
from typing import Callable
from functools import wraps

count = 0
_redis = redis.Redis()


# def get_page(url: str) -> str:
#     """Obtains the HTML content of a particular URL and returns it.
#     Tracks how many times the URL was accessed and storesp this
#     count in a Redis cache.
#     """
#     cache.set(f"cached:{url}", count)
#     respp = requests.get(url)
#     cache.incr(f"count:{url}")
#     cache.setex(f"count:{url}", 10, cache.get(f"cached:{url}"))
#     return respp.text


# if __name__ == "__main__":
#     url_ = "http://slowwly.robertomurray.co.uk/delay/1000/url/"
#     url = f"{url_}http://www.google.com"
#     print(get_page(url))
#     print(get_page(url))
#     print(f"Access count for {url}: {count}")

def cache_url(method: Callable[..., str]) -> Callable[..., str]:
    """Decorator to Cache URLS """

    @wraps(method)
    def wrapper(url: str, *args, **kwd) -> str:
        """wraps a function to cache urls"""
        key = f"cache:{url}"
        cache = _redis.get(key)
        resp = method(url, *args, **kwd)
        if cache:
            return resp
        _redis.setex(key, 10, resp)
        return resp
    return wrapper


def count_calls(method: Callable[..., str]) -> Callable[..., str]:
    """ Decorator: counts number of times a method is called """

    @wraps(method)
    def wrapper(url: str, *args, **kwd) -> str:
        """ Wrapper function """
        key = f"count:{url}"
        _redis.incr(key, 1)
        return method(url, *args, **kwd)
    return wrapper


@cache_url
@count_calls
def get_page(url: str) -> str:
    """fetch data from url using requests module"""
    resp = requests.get(url)
    return resp.text
