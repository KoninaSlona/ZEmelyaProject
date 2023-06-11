"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections.abc import Callable


def cache(func: Callable) -> Callable:
     # Create a dictionary to store cached values
    cache = {}

    def cached_func(*args):
        # Check if the arguments are already in the cache
        if args in cache:
            # Return the cached result
            return cache[args]
        
        # If the arguments are not in the cache, call the original function
        result = func(*args)
        
        # Cache the result for future use
        cache[args] = result
        
        # Return the result
        return result

    # Return the cached function
    return cached_func
