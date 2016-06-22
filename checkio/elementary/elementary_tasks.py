def fizz_buzz():
    """
    https://checkio.org/mission/fizz-buzz/
    "Fizz Buzz" if the number is divisible by 3 and by 5;
    "Fizz" if the number is divisible by 3;
    "Buzz" if the number is divisible by 5;
    """
    def checkio(number):
        if number % 5 == 0 and number % 3 == 0:
            return "Fizz Buzz"
        elif number % 3 == 0:
            return "Fizz"
        elif number % 5 == 0:
            return "Buzz"
        return str(number)

    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "5 is divisible by 5"
    assert checkio(7) == "7", "7 is not divisible by 3 or 5"


def index_power():
    """
    https://checkio.org/mission/index-power/
    You are given an array with positive numbers and a number N.
    You should find the N-th power of the element in the array with the index N.
    If N is outside of the array, then return -1. Don't forget that the first
    element has the index 0.

    Let's look at a few examples:
    - array = [1, 2, 3, 4] and N = 2, then the result is 32 == 9;
    - array = [1, 2, 3] and N = 3, but N is outside of the array,
    the result is -1.
    """
    def index_power(array, n):
        """
        Find Nth power of the element with index N.
        """
        try:
            return array[n]**n
        except IndexError:
            return -1

    assert index_power([1, 2, 3, 4], 2) == 9, "Square"
    assert index_power([1, 3, 10, 100], 3) == 1000000, "Cube"
    assert index_power([0, 1], 0) == 1, "Zero power"
    assert index_power([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 9)


def even_last():
    """
    https://checkio.org/mission/even-last/
    You are given an array of integers. You should find the sum of the elements
    with even indexes (0th, 2nd, 4th...) then multiply this summed number and
    the final element of the array together. Don't forget that the first element
    has an index of 0. For an empty array, the result will always be 0 (zero).
    """

    def checkio(array):
        """
        Sums even-indexes elements and multiply at the last
        """
        return sum([item for item in array[::2]]) *  array[-1] if array else 0

    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"


def monkey_typing():
    """
    https://checkio.org/mission/monkey-typing/
    You are given some text potentially including sensible words.
    You should count how many words are included in the given text.
    A word should be whole and may be a part of other word. Text letter case
    does not matter. Words are given in lowercase and don't repeat.
    If a word appears several times in the text, it should be counted only once.

    For example, text - "How aresjfhdskfhskd you?",
    words - ("how", "are", "you", "hello"). The result will be 3.
    """
    def count_words(text, words):
        return len([word for word in words if word in text.lower()])

    assert count_words("How aresjfhdskfhskd you?",
                       {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!",
                       {"banana", "bananas"}) == 2, "BANANAS!"


def secret_message():
    """
    https://checkio.org/mission/secret-message/
    You are given a chunk of text. Gather all capital letters in one word in
    the order that they appear in the text.

    For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.",
    if we collect all of the capital letters, we get the message "HELLO".
    """
    def find_message(text):
        return "".join([letter for letter in text if letter.isupper()])

    assert find_message(
        "How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"


def three_words():
    """
    https://checkio.org/mission/three-words/
    ou are given a string with words and numbers separated by whitespaces
    (one space). The words contains only letters. You should check if the string
    contains three words in succession. For example, the string "start
    5 one two three 7 end" contains three words in succession.
    """

    def checkio(words):
        return '111' in "".join(
            ['0' if w.isdigit() else '1' for w in words.split()])

    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"


def most_numbers():
    """
    https://checkio.org/mission/most-numbers/
    You are given an array of numbers (floats). You should find the difference
    between the maximum and minimum element. Your function should be able to
    handle an undefined amount of arguments. For an empty argument list,
    the function should return 0.

    Floating-point numbers are represented in computer hardware as base 2
    fractions (read about this here). So we should check the result
    with ±0.001 precision.
    Think about how to work with an arbitrary number of arguments.
    """
    def checkio(*args):
        return max(args) - min(args) if args else 0

    def almost_equal(checked, correct, significant_digits):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(checkio(1, 2, 3), 2, 3), "3-1=2"
    assert almost_equal(checkio(5, -5), 10, 3), "5-(-5)=10"


def boolean_algebra():
    """
    https://checkio.org/mission/boolean-algebra/
    In this mission you should implement some boolean operations:
    - "conjunction" denoted x ∧ y, satisfies x ∧ y = 1 if x = y = 1
        and x ∧ y = 0 otherwise.
    - "disjunction" denoted x ∨ y, satisfies x ∨ y = 0 if x = y = 0
        and x ∨ y = 1 otherwise.
    - "implication" (material implication) denoted x→y and can be described
            as ¬ x ∨ y. If x is true then the value of x → y is taken to be that
            of y. But if x is false then the value of y can be ignored;
            however the operation must return some truth value and there are
            only two choices, so the return value is the one that entails less,
            namely true.
    - "exclusive" (exclusive or) denoted x ⊕ y and can be described as
            (x ∨ y)∧ ¬ (x ∧ y). It excludes the possibility of both x and y.
            Defined in terms of arithmetic it is addition mod 2 where 1 + 1 = 0.
    - "equivalence" denoted x ≡ y and can be described as ¬ (x ⊕ y).
        It's true just when x and y have the same value.
    """

    def boolean(x, y, operation):
        operation_map = {
            'conjunction': lambda x, y: x & y,
            'disjunction': lambda x, y: x | y,
            'implication': lambda x, y: (1 - x) | y,
            'exclusive':   lambda x, y: x ^ y,
            'equivalence': lambda x, y: x == y
        }
        return operation_map[operation](x, y)

    assert boolean(1, 0, u"conjunction") == 0, "and"
    assert boolean(1, 0, u"disjunction") == 1, "or"
    assert boolean(1, 1, u"implication") == 1, "material"
    assert boolean(0, 1, u"exclusive") == 1, "xor"
    assert boolean(0, 1, u"equivalence") == 0, "same?"


def digits_multiplication():
    """
    https://checkio.org/mission/digits-multiplication/
    You are given a positive integer. Your function should calculate the product
    of the digits excluding any zeroes. For example: The number given is
    123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).
    """
    import operator
    from functools import reduce

    def checkio(number):
        return reduce(operator.mul,
                      [int(num) for num in str(number) if int(num) > 0])

    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1


def end_of_other():
    """
    https://checkio.org/mission/end-of-other/
    In this task, you are given a set of words in lower case. Check whether
    there is a pair of words, such that one word is the end of another
    (a suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the
    end of "hello", so the result is True.
    Input: Words as a set of strings. Output: True or False, as a boolean.
    """
    from itertools import permutations

    def checkio(words_set):
        return any([w[0].endswith(w[1]) for w in permutations(words_set, 2)])

    assert checkio({"hello", "lo", "he"}) == True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
    assert checkio({"one"}) == False, "Only One"
    assert checkio({"helicopter", "li", "he"}) == False, "Only end"


def days_diff():
    """
    https://checkio.org/mission/days-diff/
    Input: Two dates as tuples of integers.
    Output: The difference between the dates in days as an integer.
    Precondition: Dates between 1 january 1 and 31 december 9999.
    """
    from datetime import date
    def days_diff(date1, date2):
        return abs((date(*date1) - date(*date2)).days)

    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238


def count_inversions():
    """
    https://checkio.org/mission/count-inversions
    Check out this example sequence: (1, 2, 5, 3, 4, 7, 6) and we can see
    here three inversions - 5 and 3; - 5 and 4; - 7 and 6.
    You are given a sequence of unique numbers and you should count the number
    of inversions in this sequence.
    Input: A sequence as a tuple of integers.
    Output: The inversion number as an integer.
    """
    from itertools import combinations
    def count_inversion(sequence):
        """
        Count inversions in a sequence of numbers
        """
        return [c[0] > c[1] for c in combinations(sequence, 2)].count(True)

    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"

if __name__ == "__main__":
    fizz_buzz()
    index_power()
    even_last()
    monkey_typing()
    secret_message()
    three_words()
    most_numbers()
    boolean_algebra()
    digits_multiplication()
    end_of_other()
    days_diff()
    count_inversions()