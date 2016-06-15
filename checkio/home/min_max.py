"""
In this mission you should write you own py3 implementation (
but you can use py2 for this) of the built-in functions min and max.
Some builtin functions are closed here: import, eval, exec, globals.
Don't forget you should implement two functions in your code.

max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])

Input: One positional argument as an iterable or two or more positional
arguments. Optional keyword argument as a function.

Output: The largest item for the "max" function and the smallest for
the "min" function.

Example:

max(3, 2) == 3
min(3, 2) == 2
max([1, 2, 0, 3, 4]) == 4
min("hello") == "e"
max(2.2, 5.6, 5.9, key=int) == 5.6
min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]

"""


def min(*args, **kwargs):
    key = kwargs.get("key", None)
    args = args[0] if len(args) == 1 else args
    return sorted(args, key=key)[0]


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    args = args[0] if len(args) == 1 else args
    return sorted(args, key=key, reverse=True)[0]


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"