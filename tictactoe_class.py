# Tictactoe with classes.
# need to read more OOP stuff.
# right now i'm just translating my old program to classes.
# not fully thinking about how to implement classes.



import copy
import random
import itertools





class Board:
    empty_board = [['-' for i in range(3)] for j in range(3)]
    def __init__(self, board=empty_board, p1='x', p2='o'):
        self.board = board
        self.p1, self.p2 = p1, p2
        self.cols = None
        self.diags = None
        self.empty_spots = list(itertools.product(range(3), range(3)))

    def update_cols(self):
        self.cols = [[row[i] for row in self.board] for i in range(3)]

    def update_diags(self):
        maindiag = [self.board[i][i] for i in range(3)]
        oppdiag = [self.board[i][2-i] for i in range(3)]
        self.diags = [maindiag, oppdiag]

    def update_board(self, row, col, p):
        self.board[row][col] = p
        self.update_cols()
        self.update_diags()
        self.update_empty_spots()

    def print_board(self):
        """Prints a pretty version of board."""
        board_string = (
        '{0[0]:^3}|{0[1]:^3}|{0[2]:^3}'
        '\n-----------\n'
        '{1[0]:^3}|{1[1]:^3}|{1[2]:^3}'
        '\n-----------\n'
        '{2[0]:^3}|{2[1]:^3}|{2[2]:^3}'
        )
        print(board_string.format(*self.board))

    def is_empty(self, row, col):
        return self.board[row][col] == '-'

    def update_empty_spots(self):
        """
        Return tuples (row, col) of all empty spots in board.
        """
        products = itertools.product(range(3), range(3))
        self.empty_spots =  [prod for prod in products if self.is_empty(*prod)]

    def check_for_win(self, p):
        """
        Return True if p won.
        """
        #check rows.
        for row in self.board:
            if set(row) == set(p):
                return True

        #check columnss.
        for col in self.cols:
            if set(col) == set(p):
                return True

        #check diagonal.
        for diag in self.diags:
            if set(diag) == set(p):
                return True

        #no winner found.
        return False



def is_winning_move(board, row, col, p):
    """
    Check if p wins by picking spot board[row][col].
    """
    new_board = Board(board=copy.deepcopy(board.board))
    new_board.update_board(row, col, p)
    return new_board.check_for_win(p)


def get_winning_moves(board, p):
    """
    Return a list of winning moves for p.
    """
    empty_spots = board.empty_spots
    return [(i, j) for (i,j) in empty_spots if is_winning_move(board, i, j, p)]



class Player(Board):
    def __init__(self, char):
        self.char = char

    def is_winning_move(self, board, row, col):
        """
        Check if player wins by picking spot board[row][col].
        """
        new_board = Board(board=copy.deepcopy(board.board))
        new_board.update_board(row, col, self.char)
        return new_board.check_for_win(self.char)

    def get_winning_moves(self, board):
        """
        Return a list of winning moves for player.
        """
        empty_spots = board.empty_spots
        return [(i, j) for (i,j) in empty_spots if self.is_winning_move(board, i, j)]



class Computer(Player):

    def move(self, board):
        """
        Assumes that there are global variables `comp` and `player`.

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



def player_move():
    """
    Assumes that there is a global variable `player`.
    """
    row = int(input('Pick a row: ')) - 1
    col = int(input('Pick a column: ')) - 1

    if is_empty(board, row, col):
        update(board, row, col, player)
        print('\n')
    else:
        print('\nSpot not empty. Try again.')
        player_move()

    print('Current Board:')
    print_board(board)
    print('\n')


def game():
    while True:
        computer_move()
        if check_win(board, comp):
            print('Computer wins!')
            break
        if not get_empty_spots(board):
            print("It's a draw...")
            break
        player_move()
        if check_win(board, player):
            print('Player wins!')
            break


if __name__ == '__main__':
    board = [['-' for i in range(3)] for j in range(3)]
    comp, player = 'x', 'o'
    game()
