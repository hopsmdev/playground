"""
Consider a tuple of tuples in which the first tuple has one integer and each
consecutive tuple has one more integer then the last. Such a tuple of tuples
would look like a triangle. You should write a program that will help Stephan
find the highest possible sum on the most profitable route down the pyramid.
All routes down the pyramid involve stepping down and to the left or down and
to the right.

Tips: Think of each step down to the left as moving to the same index location
or to the right as one index location higher. Be very careful if you plan to
use recursion here.

For example we have pyramids like:

(1,),
(2, 3),
(3, 3, 1),
(3, 1, 5, 4),
(3, 1, 3, 1, 3),
(2, 2, 2, 2, 2, 2),
(5, 6, 4, 5, 6, 4, 3)

Maximum gold count here is 23, and path is:
(0,0) 1 -> (1,1) 3 -> (2,1) 3 -> (3,2) 5 -> (4,2) 3 -> (5,3) 2 -> (6,4) 6
and it takes 23
"""


def count_gold(pyramid):
    """
    How it works:

    For pyramid:
    (1,),
    (2, 3),
    (3, 3, 1),
    (3, 1, 5, 4),
    (3, 1, 3, 1, 3),
    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3)

    algorithm will "reduce" each row and it gives us list of row's values e.g.:

    [[23], [21, 22], [17, 19, 17], [14, 12, 16, 15], [11, 9, 11, 9, 11],
    [8, 8, 7, 8, 8, 6], [5, 6, 4, 5, 6, 4, 3]]

    First element from this list is our MAX we need to find.

    We need to iterate over pyramid backwards - from last row to first row,
    and also we need to iterate over pyramid row's columns.
    For example, let's take last row:
    (5, 6, 4, 5, 6, 4, 3) to reduce it, we also need next row so:

    (2, 2, 2, 2, 2, 2),
    (5, 6, 4, 5, 6, 4, 3)

    We need to find "small pyramids" with 3 elements:
    top element from next row, and two bottom elements from current row.
    In our example we can build 6 small pyramids from last 2 rows in pyramid:
     2     2     2     2     2     2
    5 6   6 4   4 5   5 6   6 4   4 3

    then we can reduce last row and store max values in next row -
    to reduce means find maximum from pyramid's bottom elements and store
    result as a sum of pyramid's top element and our maximum.
    pyramid[up_row][col] += max(pyramid[row][col], pyramid[row][col + 1])

    In our case we will have: 8 8 7 8 6. We need to repeat those steps until we
    reach pyramid's top element.

    :param pyramid:
    :return:
    """

    _pyramid = list(list(row) for row in pyramid)
    for row_idx in range(len(_pyramid) - 1, 0, -1):
        row = _pyramid[row_idx]
        for col_idx in range(len(row) - 1):

            next_col_idx = min(col_idx + 1, len(row) - 1)
            up_row_idx = max(row_idx - 1, 0)

            reduced_value = max(
                _pyramid[row_idx][col_idx],
                _pyramid[row_idx][next_col_idx])

            _pyramid[up_row_idx][col_idx] += reduced_value

    print(_pyramid)
    print("MAX GOLD: ", _pyramid[0][0])
    return _pyramid[0][0]


if __name__ == '__main__':

    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"

    assert count_gold((
        (2,),
        (7, 9),
        (0, 8, 6),
        (4, 7, 6, 8),
        (0, 5, 5, 4, 1),
        (9, 1, 0, 1, 6, 9))) == 35, "fourth example"

    assert count_gold((
        [4],
        [1, 7],
        [9, 9, 7],
        [4, 9, 9, 3],
        [3, 5, 3, 7, 5],
        [1, 7, 5, 3, 5, 6],
        [6, 5, 5, 8, 3, 3, 3],
        [6, 8, 6, 8, 7, 3, 7, 5],
        [7, 9, 9, 1, 6, 8, 7, 5, 9],
        [2, 8, 2, 5, 5, 5, 2, 5, 7, 8],
        [1, 3, 5, 2, 4, 5, 3, 5, 1, 1, 6],
        [8, 6, 1, 1, 3, 4, 7, 5, 3, 6, 1, 9],
        [5, 8, 6, 6, 2, 6, 9, 3, 7, 4, 6, 9, 9],
        [3, 3, 5, 4, 4, 6, 9, 2, 5, 7, 7, 1, 6, 7],
        [8, 1, 4, 4, 6, 8, 4, 9, 7, 6, 1, 8, 4, 2, 9],
        [6, 5, 8, 6, 8, 3, 2, 4, 8, 8, 1, 5, 6, 8, 8, 7],
        [6, 3, 9, 1, 5, 6, 7, 7, 2, 2, 6, 2, 2, 1, 8, 8, 6],
        [4, 7, 8, 7, 5, 2, 8, 8, 2, 2, 7, 1, 3, 8, 1, 9, 4, 7],
        [1, 7, 8, 1, 4, 3, 8, 6, 6, 9, 6, 3, 5, 4, 7, 6, 4, 5, 6],
        [1, 1, 4, 9, 9, 8, 3, 3, 8, 1, 8, 1, 7, 6, 6, 3, 2, 1, 1, 6],
    )) == 139, 'Veeeery big pyramid'