""""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any


def combinations(*args: List[Any]) -> List[List]:
     # Base case: If there is only one list in args, return a list of individual elements
    if len(args) == 1:
        return [[item] for item in args[0]]
    
    # Recursive case: Combine the first list with combinations of the remaining lists
    sub_combinations = combinations(*args[1:])
    result = []
    for item in args[0]:
        for sub_combination in sub_combinations:
            result.append([item] + sub_combination)
    return result
