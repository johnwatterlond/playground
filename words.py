"""
To use:
from words import word_list
"""

def get_word_list():
    """Return set of words from think_python dictionary."""
    word_list = []
    with open('words.txt') as f:
        for line in f:
            word_list.append(line.strip())
    return word_list


word_list = get_word_list()
