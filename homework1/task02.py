"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence

We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections.abc import Sequence

def check_fibonacci(data: Sequence[int]) -> bool:
    if len(data) == 0:
        return False
    if (data[0] != 0):
        return False
    if (len(data) >= 2 and data[1] != 1):
        return False
    for index in range(2, len(data)) :
        if data[index] != (data[index-1] + data[index-2]):
            return False
    return True