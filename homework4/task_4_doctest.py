"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


>>> fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    fizzbuzz_list = []  # Create an empty list to store the FizzBuzz numbers
    for i in range(1, n + 1):  # Iterate from 1 to n (inclusive)
        if i % 3 == 0 and i % 5 == 0:  # If the number is divisible by both 3 and 5
            fizzbuzz_list.append("fizzbuzz")  # Append "fizzbuzz" to the list
        elif i % 3 == 0:  # If the number is divisible by 3
            fizzbuzz_list.append("fizz")  # Append "fizz" to the list
        elif i % 5 == 0:  # If the number is divisible by 5
            fizzbuzz_list.append("buzz")  # Append "buzz" to the list
        else:
            fizzbuzz_list.append(str(i))  # Append the number as a string to the list
    return fizzbuzz_list  # Return the list of FizzBuzz numbers