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

