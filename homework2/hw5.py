"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
from typing import Iterable, List


def custom_range(iterable: Iterable, start=None, stop=None, step=None) -> List:
    # Convert the iterable to a list
    iterable_list = list(iterable)
    
    # Handle the case when no arguments are provided
    if start is None:
        return iterable_list
    
    # Get the index of the start value
    start_index = iterable_list.index(start)
    
    # Get the index of the stop value
    if stop is None:
        stop_index = len(iterable_list)
    else:
        stop_index = iterable_list.index(stop)
    
    # Handle the case when step is not provided
    if step is None:
        step = 1
    
    # Get the sublist based on the start, stop, and step values
    sublist = iterable_list[start_index:stop_index:step]
    
    return sublist