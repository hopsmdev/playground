"""
Chess is a two-player strategy game played on a checkered game board laid out
in eight rows (called ranks and denoted with numbers 1 to 8) and eight columns
(called files and denoted with letters a to h) of squares. Each square of the
chessboard is identified by a unique coordinate pair — a letter and a number
(ex, "a1", "h8", "d6"). For this mission we only need to concern ourselves with
pawns. A pawn may capture an opponent's piece on a square diagonally in front
of it on an adjacent file, by moving to that square. For white pawns the front
squares are squares with greater row than their.

A pawn is generally a weak unit, but we have 8 of them which we can use to
build a pawn defense wall. With this strategy, one pawn defends the others.
A pawn is safe if another pawn can capture a unit on that square.
We have several white pawns on the chess board and only white pawns.
You should design your code to find how many pawns are safe.

You are given a set of square coordinates where we have placed white pawns.
You should count how many pawns are safe.

Input: Placed pawns coordinates as a set of strings.

Output: The number of safe pawns as a integer.

Example:

safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
"""

import string
import itertools

def safe_pawns_oneliner(pawns):

    return len([pawn for pawn in pawns if
                chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1) in pawns or
                chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1) in pawns])

def safe_pawns_simple(pawns):

    safe_counter = 0
    for pawn in pawns:
        left_defence = chr(ord(pawn[0]) - 1) + str(int(pawn[1]) - 1)
        right_defence = chr(ord(pawn[0]) + 1) + str(int(pawn[1]) - 1)

        if left_defence in pawns or right_defence in pawns:
            safe_counter += 1

    return safe_counter


def safe_pawns(p):

    columns = string.ascii_lowercase[:8]

    safe_pawns_list = []

    permutations = [item for item in itertools.permutations(p, 2)
                    if item[0][1] > item[1][1]]

    for pawns_permutation in permutations:

        pawn1, pawn2 = pawns_permutation

        col1, rank1 = pawn1
        col2, rank2 = pawn2

        col_left = columns[max(columns.index(col1) - 1, 0)]
        col_right = columns[min(columns.index(col1) + 1, len(columns) - 1)]

        if col2 in (col_left, col_right) and col2 != col1 \
                and int(rank1) -1 == int(rank2):
            safe_pawns_list.append(pawn1)

    return len(set(safe_pawns_list))


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns_simple({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns_simple({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns_simple({"a1", "a2", "a3", "a4", "h1", "h2", "h3", "h4"}) \
           == 0

