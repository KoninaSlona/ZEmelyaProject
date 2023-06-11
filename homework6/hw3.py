"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    def check_rows():
        for row in board:
            if all(cell == 'x' for cell in row):
                return 'x wins!'
            elif all(cell == 'o' for cell in row):
                return 'o wins!'
        return None

    def check_columns():
        for col in range(3):
            if all(board[row][col] == 'x' for row in range(3)):
                return 'x wins!'
            elif all(board[row][col] == 'o' for row in range(3)):
                return 'o wins!'
        return None

    def check_diagonals():
        if board[0][0] == board[1][1] == board[2][2] == 'x':
            return 'x wins!'
        elif board[0][0] == board[1][1] == board[2][2] == 'o':
            return 'o wins!'
        elif board[0][2] == board[1][1] == board[2][0] == 'x':
            return 'x wins!'
        elif board[0][2] == board[1][1] == board[2][0] == 'o':
            return 'o wins!'
        return None

    def check_draw():
        if all(cell != '-' for row in board for cell in row):
            return 'draw!'
        return None

    # Проверяем выигрышные комбинации
    result = check_rows() or check_columns() or check_diagonals()
    if result:
        return result

    # Проверяем ничью
    result = check_draw()
    if result:
        return result

    # Если нет выигрышных комбинаций и ничьи, значит игра не завершена
    return 'unfinished'
