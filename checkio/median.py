"""
A median is a numerical value separating the upper
half of a sorted array of numbers from the lower half.
In a list where there are an odd number of entities,
the median is the number found in the middle of the array.
If the array contains an even number of entities,
then there is no single middle value, instead the median becomes the average
of the two numbers found in the middle.
For this mission, you are given a non-empty array of natural numbers (X).
With it, you must separate the upper half of t
he numbers from the lower half and find the median.

Input: An array as a list of integers.

Output: The median as a float or an integer.

Example:

checkio([1, 2, 3, 4, 5]) == 3
checkio([3, 1, 2, 5, 3]) == 3
checkio([1, 300, 2, 200, 1]) == 2
checkio([3, 6, 20, 99, 10, 15]) == 12.5
"""

def checkio(data):

    # simplest solution
    #from statistics import median
    #return median(data)

    data.sort()
    data_length = len(data)
    if data_length % 2 == 1:
        return data[data_length // 2]

    if data_length % 2 == 0:
        half = data_length // 2
        return (data[half - 1] + data[half]) / 2

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 2, 3, 4, 5]) == 3, "Sorted list"
    assert checkio([3, 1, 2, 5, 3]) == 3, "Not sorted list"
    assert checkio([1, 300, 2, 200, 1]) == 2, "It's not an average"
    assert checkio([3, 6, 20, 99, 10, 15]) == 12.5, "Even length"
    print("Start the long test")
    assert checkio(list(range(1000000))) == 499999.5, "Long."
    print("The local tests are done.")