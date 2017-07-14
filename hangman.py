"""
A hangman game.

Player is allowed 7 wrong guesses.
"""

import string
import os
import random

from words import word_list


def clear():
    """Clear terminal screen."""
    os.system('clear')


class Hangman:
    """
    Represents a game of hangman.

    Args:
        secret_word: The word used for the game of hangman.

    Attributes:
        secret_word: The word used for the game of hangman.
        board_list: List representing current board. Missing letters
                        are indicated by '-'.
        guesses: List of guesses made.
        guesses_left: Number of guesses left. Only changes if an
                        incorrect guess is made.
        last_guess: String holding the last guess made.
        message: String used to print a message to the screen.
    """
    def __init__(self, secret_word):
        self.secret_word = secret_word
        self.board_list = ['-' for letter in secret_word]
        self.guesses = []
        self.guesses_left = 7
        self.last_guess = ''
        self.message = ''

    def update_board(self, letter):
        """Update board with letter."""
        for index, secret_letter in enumerate(self.secret_word):
            if secret_letter == letter:
                self.board_list[index] = letter

    def update_guesses(self, letter):
        """Update the list of letters already tried."""
        self.guesses.append(letter)

    def update_guesses_left(self):
        """Update the number of guesses left."""
        self.guesses_left = self.guesses_left - 1

    def update_last_guess(self, letter):
        """Update the last guess to letter."""
        self.last_guess = letter

    def board_empty(self):
        """Return True if the board is empty (word guessed)."""
        return not '-' in self.board_list

    def print_board(self):
        """
        Print out the current board and info about it.

        Clears out terminal screen.
        """
        clear()
        print('Current board:')
        print(''.join(self.board_list))
        print()
        print('Number of guesses left: {}'.format(self.guesses_left))
        print('Last guess was: {}'.format(self.last_guess))
        print('Guesses so far: {}\n'.format(' '.join(self.guesses)))
        print('{}'.format(self.message))

    def prompt_letter(self):
        """
        Prompt the user for a letter.

        Checks that given character is a single letter and that it
        hasn't already been guessed.
        """
        while True:
            letter = input('Guess a letter.\n').lower()
            if letter not in list(string.ascii_letters):
                print('\nInvalid input. Try again.')
            elif letter in self.guesses:
                print('\nAlready guessed {}. Try again.'.format(letter))
            else:
                break
        return letter

    def take_turn(self):
        """
        Take a turn.

        Prompt user for letter. Update board and letters that have
        already been tried.  Also update the number of guesses left.

        If game is over, prints the appropriate message.
        """

        # print board and prompt user for letter.
        self.print_board()
        letter = self.prompt_letter()

        # update list of guesses and last guess.
        self.update_guesses(letter)
        self.update_last_guess(letter)

        # process guess.
        if letter in self.secret_word:
            self.update_board(letter)
        else:
            self.update_guesses_left()

        # check for and process end of game.
        if self.board_empty():
            self.message = 'Congrats you win!'
            self.print_board()
        elif not self.guesses_left:
            self.message = (
            'No more guesses left. You lose.'
            '\n'
            'The word was {}.'
            ).format(self.secret_word)
            self.print_board()

    def play_game(self):
        """Play hangman."""
        while self.guesses_left and not self.board_empty():
            self.take_turn()


def main():
    """
    Grab a secret_word from word_list and start a game of hangman.
    """
    secret_word = random.choice(word_list)

    hangman = Hangman(secret_word)
    hangman.play_game()


if __name__ == '__main__':
    main()
