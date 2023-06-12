from functools import wraps
from collections.abc import Callable


def cache(times: int) -> Callable:
    def decorator(func):
        cached_results = {}
        remaining_times = times

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal remaining_times

            # Convert args and kwargs into a hashable key
            key = (args, frozenset(kwargs.items()))

            # If the result for the key is already in cache and there are remaining times, return it
            if key in cached_results and remaining_times > 0:
                remaining_times -= 1
                return cached_results[key]

            # Invoke the original function and store the result in cache
            result = func(*args, **kwargs)
            cached_results[key] = result
            return result

        return wrapper

    return decorator