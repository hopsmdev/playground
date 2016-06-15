"""
Tic-Tac-Toe, sometimes also known as Xs and Os, is a game for two players
(X and O) who take turns marking the spaces in a 3×3 grid.
The player who succeeds in placing three respective marks in a horizontal,
vertical, or diagonal rows (NW-SE and NE-SW) wins the game.

But we will not be playing this game. You will be the referee for
this games results. You are given a result of a game and you must determine
if the game ends in a win or a draw as well as who will be the winner.
Make sure to return "X" if the X-player wins and "O" if the O-player wins.
If the game is a draw, return "D".
"""

def checkio(game_result):

    winner_marks_list = [
        [(0,0), (0,1), (0,2)],
        [(1,0), (1,1), (1,2)],
        [(2,0), (2,1), (2,2)],
        [(0,0), (1,0), (2,0)],
        [(0,1), (1,1), (2,1)],
        [(0,2), (1,2), (2,2)],
        [(0,0), (1,1), (2,2)],
        [(0,2), (1,1), (2,0)]
    ]

    for marks in winner_marks_list:

        mark_list = [game_result[row][col] for row, col in marks]

        if mark_list.count('X') == 3:
            return 'X'
        elif mark_list.count('O') == 3:
            return 'O'

    return 'D'

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"

