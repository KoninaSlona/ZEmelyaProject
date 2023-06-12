"""
Given two strings. Return if they are equal when both are typed into
empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Examples:
    Input: s = "ab#c", t = "ad#c"
    Output: True
    # Both s and t become "ac".

    Input: s = "a##c", t = "#a#c"
    Output: True
    Explanation: Both s and t become "c".

    Input: a = "a#c", t = "b"
    Output: False
    Explanation: s becomes "c" while t becomes "b".

"""


def backspace_compare(first: str, second: str) -> bool:
    # Внутренняя функция для обработки строки
    def process_string(s: str) -> str:
        stack = []  # Инициализация стека
        for char in s:
            if char != '#':  # Если символ не backspace, добавляем его в стек
                stack.append(char)
            elif stack:  # Если стек не пустой, удаляем последний символ из стека
                stack.pop()
        return ''.join(stack)  # Возвращаем обработанную строку без символов backspace
    
    # Сравниваем обработанные строки first и second
    return process_string(first) == process_string(second)
