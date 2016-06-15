"""A binary gap within a positive integer N is any maximal sequence of
consecutive zeros that is surrounded by ones at both ends in the binary
representation of N.

For example, number 9 has binary representation 1001 and contains a binary
gap of length 2. The number 529 has binary representation 1000010001 and
contains two binary gaps: one of length 4 and one of length 3.
The number 20 has binary representation 10100 and contains one binary gap of
length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

def solution(N)
that, given a positive integer N, returns the length of its longest binary gap.
The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary
representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

N is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(log(N));
expected worst-case space complexity is O(1).
"""

import re
from utils.execution_time import execution_time

TEST_LOOPS = 1000
VERBOSE = False


@execution_time(loops=TEST_LOOPS, verbose=VERBOSE)
def solution(N):
    try:
        binary = str(bin(N))[2:]
        return len(max(binary.split('1')[1:-1]))
    except (TypeError, ValueError):
        return 0


@execution_time(loops=TEST_LOOPS, verbose=VERBOSE)
def solution_regex(N):
    try:
        binary = str(bin(N))[2:]
        r = re.compile("(?<=1{1})([0]+)+(?=1{1})")
        return len(max(r.findall(binary)))
    except (TypeError, ValueError):
        return 0


def speed_tests(fn):
    fn(1073741825)
    fn(20)
    fn(328)


def assert_test(fn):
    assert fn(328) == 2, '101001000'
    assert fn(1) == 0, '1'
    assert fn(9) == 2, '1001'
    assert fn(529) == 4, '1000010001'
    assert fn(1041) == 5, '10000010001'
    assert fn(6) == 0, '110'
    assert fn(51712) == 2, '110010100000000'
    assert fn(20) == 1, '10100'
    assert fn(1073741825) == 29, '1000000000000000000000000000001'


if __name__ == '__main__':
    speed_tests(solution)
    print()
    speed_tests(solution_regex)

    #assert_test(solution_regex)

"""
Results:

[solution] avg execution time: 4.4517400237964466e-06 s, loops: 100
[solution] avg execution time: 4.131880705244839e-06 s, loops: 100
[solution] avg execution time: 4.720519646070898e-06 s, loops: 100

[solution_regex] avg execution time: 1.1620090081123635e-05 s, loops: 100
[solution_regex] avg execution time: 3.668469798867591e-06 s, loops: 100
[solution_regex] avg execution time: 4.620920080924407e-06 s, loops: 100

"""
