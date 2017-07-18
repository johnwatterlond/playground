"""
tictactoe!

Very simple tictactoe game.
Throughout this script, the variable `board` is a list containing the rows of a tictactoe board.
"""

import copy
import random
import itertools
import os


def clear():
    """Clear terminal screen."""
    os.system('clear')


def cols(board):
    """
    Return columns of board as a list.
    """
    return [[row[i] for row in board] for i in range(3)]


def diags(board):
    """
    Return diagonals of board as a list.
    """
    maindiag = [board[i][i] for i in range(3)]
    oppdiag = [board[i][2-i] for i in range(3)]
    return [maindiag, oppdiag]


def is_empty(board, row, col):
    return board[row][col] == '-'


def get_empty_spots(board):
    """
    Return tuples (row, col) of all empty spots in board.
    """
    products = itertools.product(range(3), range(3))
    return [prod for prod in products if is_empty(board, *prod)]


def update(board, row, col, char):
    board[row][col] = char


def move(board, row, col, char):
    """
    Returns a board with board[row][col] = char.
    Does not change the variable `board`.

    Assumes that board[row][col] is empty.
    """
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = char
    return board_copy


def is_winning_move(board, row, col, p):
    """
    Check if p wins by picking spot board[row][col].
    """
    _board = move(board, row, col, p)
    return check_win(_board, p)


def get_winning_moves(board, p):
    """
    Return a list of winning moves for p.
    """
    empty_spots = get_empty_spots(board)
    return [(i, j) for (i,j) in empty_spots if is_winning_move(board, i, j, p)]


def check_win(board, p):
    """
    Return True if p won.
    """
    #check rows.
    for row in board:
        if set(row) == set(p):
            return True

    #check columnss.
    for col in cols(board):
        if set(col) == set(p):
            return True

    #check diagonal.
    for diag in diags(board):
        if set(diag) == set(p):
            return True

    #no winner found.
    return False


def print_board(board):
    """
    Prints a pretty version of board.
    """
    clear()
    board_string = (
    '{0[0]:^3}|{0[1]:^3}|{0[2]:^3}'
    '\n-----------\n'
    '{1[0]:^3}|{1[1]:^3}|{1[2]:^3}'
    '\n-----------\n'
    '{2[0]:^3}|{2[1]:^3}|{2[2]:^3}'
    )
    print('Current board:')
    print(board_string.format(*board))


def computer_move():
    """
    Assumes that there are global variables `comp` and `player`.
    Assumes there is a variable `board`.

    Check if comp has any winning moves and picks one.
    Check if player has winning moves and picks one.
    Else picks a random move.
    """
    winning_moves = get_winning_moves(board, comp)
    opp_winning_moves = get_winning_moves(board, player)

    if winning_moves:
        row, col = random.choice(winning_moves)
        update(board, row, col, comp)
    elif opp_winning_moves:
        row, col = random.choice(opp_winning_moves)
        update(board, row, col, comp)
    else:
        row, col = random.choice(get_empty_spots(board))
        update(board, row, col, comp)


def player_move(player):
    """
    Assumes there is a variable `board`.
    """
    print('{} pic a move.'.format(player))
    row = int(input('Pick a row: ')) - 1
    col = int(input('Pick a column: ')) - 1

    if is_empty(board, row, col):
        update(board, row, col, player)
        print('\n')
    else:
        print('\nSpot not empty. Try again.')
        player_move(player)


def game_vs_comp():
    while True:
        print_board(board)
        computer_move()

        if check_win(board, comp):
            print_board(board)
            print('Computer wins!')
            break
        if not get_empty_spots(board):
            print_board(board)
            print("It's a draw...")
            break

        print_board(board)
        player_move(player)

        if check_win(board, player):
            print_board(board)
            print('Player wins!')
            break


def two_player_game():
    while True:
        print_board(board)
        player_move(p1)

        if check_win(board, p1):
            print_board(board)
            print('{} wins!'.format(p1))
            break
        if not get_empty_spots(board):
            print_board(board)
            print("It's a draw...")
            break

        print_board(board)
        player_move(p2)

        if check_win(board, p2):
            print_board(board)
            print('{} wins!'.format(p2))
            break


if __name__ == '__main__':
    board = [['-' for i in range(3)] for j in range(3)]
#    comp, player = 'x', 'o'
    p1, p2 = 'x', 'o'
    two_player_game()
