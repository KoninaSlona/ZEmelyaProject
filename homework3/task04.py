"""
Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
https://en.wikipedia.org/wiki/Narcissistic_number

Examples:

- 9 is an Armstrong number, 9 = 9^1 = 9
- 10 is not: 10 != 1^2 + 0^2 = 1
- 153 is : 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153


Write a function that detects if a number is Armstrong number in functionaly style:
 - use map or other utilities from functools library,
 - use anonymous functions (or use function as argument)
 - do not use loops, preferably using list comprehensions

### Example function signature and call
"""
from functools import reduce

def is_armstrong(number: int) -> bool:
    # Convert the number to a string to iterate over its digits
    digits = list(str(number))
    
    # Calculate the power to raise each digit to
    power = len(digits)
    
    # Use map to apply the power operation to each digit
    powered_digits = map(lambda x: int(x) ** power, digits)
    
    # Use reduce to sum up all the powered digits
    sum_of_digits = reduce(lambda x, y: x + y, powered_digits)
    
    # Check if the sum of digits is equal to the original number
    return sum_of_digits == number

# Test cases
  
assert is_armstrong(153) == True, 'Is Armstrong number'
assert is_armstrong(10) == False, 'Is not Armstrong number'
