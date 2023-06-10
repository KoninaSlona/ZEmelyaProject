"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List
import string


def get_longest_diverse_words(file_path: str) -> List[str]:
    # Create an empty list for words
    words = []
    with open(file_path, 'r') as file:
        # Read the text from the file
        text = file.read()
        # Split the text into words
        words = text.split()
    # Sort the words in descending order based on the number of unique symbols and length
    words = sorted(words, key=lambda x: (len(set(x)), len(x)), reverse=True)
    # Return the first 10 words with the highest number of unique symbols
    return words[:10]


def get_rarest_char(file_path: str) -> str:
    # Create a dictionary to count characters
    char_count = {}
    with open(file_path, 'r') as file:
        # Read the text from the file
        text = file.read()
        # Count the occurrences of each character
        for char in text:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
    # Find the character with the least number of occurrences
    rarest_char = min(char_count, key=char_count.get)
    return rarest_char


def count_punctuation_chars(file_path: str) -> int:
    # Initialize a counter for punctuation characters
    punctuation_count = 0
    with open(file_path, 'r') as file:
        # Read the text from the file
        text = file.read()
        # Count the number of punctuation characters
        for char in text:
            if char in string.punctuation:
                punctuation_count += 1
    return punctuation_count


def count_non_ascii_chars(file_path: str) -> int:
    # Initialize a counter for non-ASCII characters
    non_ascii_count = 0
    with open(file_path, 'r') as file:
        # Read the text from the file
        text = file.read()
        # Count the number of non-ASCII characters
        for char in text:
            if ord(char) > 127:
                non_ascii_count += 1
    return non_ascii_count


def get_most_common_non_ascii_char(file_path: str) -> str:
    # Create a dictionary to count non-ASCII characters
    non_ascii_chars = {}
    with open(file_path, 'r') as file:
        # Read the text from the file
        text = file.read()
        # Count the occurrences of each non-ASCII character
        for char in text:
            if ord(char) > 127:
                if char not in non_ascii_chars:
                    non_ascii_chars[char] = 1
                else:
                    non_ascii_chars[char] += 1
    # Find the most common non-ASCII character
    most_common_char = max(non_ascii_chars, key=non_ascii_chars.get)
    return most_common_char