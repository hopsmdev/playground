"""
Write a function that finds the longest palindromic substring of a given string.
Try to be as efficient as possible!

If you find more than one substring you should return the one which is closer
to the beginning.

Input: A text as a string.

Output: The longest palindromic substring.
"""

from itertools import combinations


def longest_palindromic(text):

    if text == text[::-1]:
        return text

    for i in range(len(text)):
        for c in combinations(text, len(text) - i):
            substr = "".join(c)
            if substr in text:
                if substr[::-1] == substr:
                    return substr

if __name__ == '__main__':
    assert longest_palindromic("artrartrt") == "rtrartr", "The Longest"
    assert longest_palindromic("abacada") == "aba", "The First"
    assert longest_palindromic("aaaa") == "aaaa", "The A"