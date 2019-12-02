import numpy as np


def calculate_neighbours(board):
    """
    Returns number of neighbours of board cells.

    Funkcja zwraca tablicę która w polu [R, C] zwraca liczbę sąsiadów którą
    ma komórka board[R, C].
    Obowiązuje sąsiedztwo Moore'a tzn. za sąsiada uznajemy żywą komórkę
    stykającą się bokiem bokach lub na ukos od danej komórki,
    więc maksymalna ilość sąsiadów danej komórki wynosi 8.
    Funkcja ta powinna być zwektoryzowana, tzn. liczba operacji w bytecodzie
    Pythona nie powinna zależeć od rozmiaru macierzy.
    (1 pkt.)

    Podpowiedź: Czy jest możliwe obliczenie ilości np. lewych sąsiadów
    których ma każda z komórek w macierzy, następnie liczby prawych sąsiadów
    itp.
    Podpowiedź II: Proszę uważać na komówki na bokach i rogach planszy.

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :param periodic
    """

    tmp = np.zeros(shape=board.shape)
    tmp[:, 1:] += board[:, :-1]  # left
    tmp[:, :-1] += board[:, 1:]  # right
    tmp[:-1, :] += board[1:, :]  # down
    tmp[1:, :] += board[:-1, :]  # up
    tmp[1:, 1:] += board[:-1, :-1]  # up left
    tmp[1:, :-1] += board[:-1, 1:]  # up right
    tmp[:-1, :-1] += board[1:, 1:]  #  down right
    tmp[:-1, 1:] += board[1:, :-1]  # down left
    return tmp


def iterate(board):
    """
    Returns next iteration step of given board.

    Funkcja pobiera planszę game of life i zwraca jej następną iterację.
    Zasady Game of life są takie:
    1. Komórka może być albo żywa (True) albo martwa (False).
    2. Jeśli komórka jest martwa i ma trzech sąsiadów to ożywa.
    3. Jeśli komórka jest żywa i ma mniej niż dwóch sąsiadów to umiera,
       jeśli ma więcej niż trzech sąsiadów również umiera.
       W przeciwnym wypadku (dwóch lub trzech sąsiadów) to żyje dalej.
    (1 pkt.)

    :param board: 2D array of agents states.
    :type board: np.ndarray
    :return: next board state
    :rtype: np.ndarray
    """
    neighbours = calculate_neighbours(board)
    dead = not board.all() # odwracam tabele
    alive = board

    # ci ktorzy ozyli
    new_guys = (neighbours == 3) & dead

    # ci ktorzy nie umarli
    old_guys = (2 <= neighbours) & (neighbours <= 3) & alive

    return new_guys | old_guys



#ważne1: bez periodycznych warunkow brzegowych
#wazne2: nie korzystac z forow tylko z dzialan macierzowych
#wazne3: wskazowka - w drugiej funkcji skorzystac z calculate
if __name__ == '__main__':
    _board = np.array([
        [False, False, False,  True, False,  True],
        [ True, False,  True, False, False,  True],
        [ True,  True, False,  True,  True,  True],
        [False,  True,  True, False, False,  True],
        [False, False, False,  True, False, False],
        [False,  True,  True,  True, False,  True]
    ])

    assert (calculate_neighbours(_board) == np.array([
        [1, 2, 2, 1, 3, 1, ],
        [2, 4, 3, 4, 6, 3, ],
        [3, 5, 5, 3, 4, 3, ],
        [3, 3, 4, 4, 5, 2, ],
        [2, 4, 6, 3, 4, 2, ],
        [1, 1, 3, 2, 3, 0, ],
    ])).all()


    assert (iterate(_board) == np.array([
        [False, False, False, False, True, False],
        [True, False, True, False, False, True],
        [True, False, False, True, False, True],
        [True, True, False, False, False, True],
        [False, False, False, True, False, False],
        [False, False, True, True, True, False],
    ])).all()


