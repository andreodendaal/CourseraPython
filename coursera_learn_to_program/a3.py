"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'OTTO')
    False
    """
    if word in wordlist:
        return True
    else:
        return False

def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B'], ['X', 'S', 'O', 'B']], 2)
    'XSOB'
    """
    board_row = board[row_index]
    make_str = ''
    for elem in board_row:
        make_str = make_str + elem

    return make_str


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['A', 'N', 'N', 'T'], ['X', 'S', 'O', 'B'], ['X', 'S', 'T', 'B']], 2)
    'NOT'
    """
    column_str = ''

    for elem in board:
        column_str = column_str + elem[column_index]

    return column_str


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'LOB')
    False
    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['D', 'O', 'G', 'B']], 'DOG')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'O', 'O', 'B']], 'NO')
    True
    """

    for iterator, elem in enumerate(board[0]):
        if word in make_str_from_column(board, iterator):
            return True

    return False


def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ELK')
    False
    """
    for row in board:
        word_construct = ''

        for elem in row:
            word_construct = word_construct + elem

        if word in word_construct:
            return True

    return False


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('DOG')
    3
    >>> word_score('NO')
    0
    >>> word_score('PHOTOGRAPHY')
    33
    """

    word_length = len(word)

    score = 0

    if word_length < 3:
        return score
    elif word_length in range(3, 7):
        score = word_length
    elif word_length in range(7, 10):
        score = word_length * 2
    elif word_length >= 10:
        score = word_length * 3

    return score



def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    """
    score = word_score(word)
    player_info[1] = player_info[1] + score


def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    >>> num_words_on_board([['A', 'N', 'T', 'D'], ['S', 'O', 'B', 'O'], ['K', 'S', 'Z', 'G']], ['ANT', 'BOX', 'SOB', 'ASK', 'DOG'])
    4
    """
    counter = 0

    for word in words:
        if board_contains_word_in_row(board, word):
            counter += 1

        if board_contains_word_in_column(board, word):
            counter += 1

    return counter



def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """
    #word_file = open(words_file)
    word_list = []

    for line in words_file:
        word_list.append(line.strip('\n'))

    return word_list

def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.
    """
    #board_file = open(board_file)

    board_list = []

    for line in board_file:

        board_list_elem = []

        for counter, elem in enumerate(line.strip('\n')):
            board_list_elem.append(elem)

        board_list.append(board_list_elem)

    return board_list

