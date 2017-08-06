"""
Module for printing a matrix.

Matrix can be of any size and can contain numbers or words of any
length.
Matrix should be a list of rows where each row is a list.


Examples:
---------

Example 1:
In :
matrix = [[2, 4, 6], [8, 10, 12], [14, 16, 18]]
print_matrix(matrix)

Out :
2   4   6
8   10  12
14  16  18


Example 2:
In :
matrix = list(zip(*[iter(range(21))]*7))
print_matrix(matrix)

Out :
0   1   2   3   4   5   6
7   8   9   10  11  12  13
14  15  16  17  18  19  20


Example 3:
In :
matrix = [
    ['cat', 'meow'],
    ['dog', 'bark'],
    ['airplane', 'vroom']
    ]
print_matrix(matrix)

Out :
cat       meow
dog       bark
airplane  vroom
"""


def get_row_format(num_cols, padding):
    """
    Return a string row_format for use in row_format.format(*row),
    where row is a row in a matrix.

    num_cols: number of columns in the matrix.
    padding: how many characters each element in the row should
    take up.
    """
    spacer = '<{}'.format(padding)
    form = '{}{}{}{}'.format('{', ':', spacer, '}')
    return '  '.join(form for x in range(num_cols))


def get_formatted_rows(matrix, num_cols, padding):
    """
    Return the rows of matrix as a list of formatted rows as
    strings.

    num_cols: number of columns in the matrix.
    padding: how many characters each element in the row should
    take up.
    """
    row_format = get_row_format(num_cols, padding)
    return [row_format.format(*row) for row in matrix]


def get_matrix_string(matrix, num_cols, padding):
    """
    Return matrix as a string ready to be printed.

    num_cols: number of columns in the matrix.
    padding: how many characters each element in the row should
    take up.
    """
    rows = get_formatted_rows(matrix, num_cols, padding)
    return '\n'.join(list(rows))


def len_longest_in_row(row):
    """
    Return the length of the longest element in row.
    """
    return max([len('{}'.format(x)) for x in row])


def get_len_longest(matrix):
    """
    Return length of the longest element in matrix.
    """
    return max([len_longest_in_row(row) for row in matrix])


def print_matrix(matrix):
    """
    Print matrix.
    """
    num_cols = len(matrix[0])
    padding = get_len_longest(matrix)
    print(get_matrix_string(matrix, num_cols, padding))
