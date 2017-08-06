


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
    Return the rows of matrix as a list of formatted rows as strings.

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
    Return the length of the longest element in list row.
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
