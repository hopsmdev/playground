"""
Roman numerals come from the ancient Roman numbering system. They are based on
specific letters of the alphabet which are combined to signify the sum
(or, in some cases, the difference) of their values.
The first ten Roman numerals are: I, II, III, IV, V, VI, VII, VIII, IX, and X.

The Roman numeral system is decimal based but not directly positional and does
not include a zero. Roman numerals are based on combinations of these
seven symbols:

Symbol Value
I 1 (unus)
V 5 (quinque)
X 10 (decem)
L 50 (quinquaginta)
C 100 (centum)
D 500 (quingenti)
M 1,000 (mille)

For this task, you should return a roman numeral using the specified integer
value ranging from 1 to 3999.

Input: A number as an integer.

Output: The Roman numeral as a string.

Example:

checkio(6) == 'VI'
checkio(76) == 'LXXVI'
checkio(13) == 'XIII'
checkio(44) == 'XLIV'
checkio(3999) == 'MMMCMXCIX'
"""


def reduce_10(number, data):
    reminder = number // 10
    if reminder > 0:  # X
        if number >= 10:
            data.append("X" * int(str(number)[0]))
        number -= reminder * 10
    print("reduce_10", number, data)
    return number


def reduce_5(number, data):
    reminder = number // 5
    if reminder > 0:  # V
        if number == 5:
            data.append("V")
        elif number == 9:
            data.append("IX")
        else:
            number -= 5
            data.append("V" + "I" * number)
    else:
        if number == 4:
            data.append("IV")
        else:
            data.append("I" * number)
    print("reduce_5", number, data)
    return number


def reduce_50(number, data):
    reminder = number // 50
    if reminder > 0:  # L
        if 90 <= number < 100:
            data.append("XC")
            number = int(str(number)[1:])
        elif 90 > number >= 50:
            data.append("L")
            number -= 50
        else:
            number = int(str(number)[1:])
    else:
        if number >= 40 < 50:
            data.append("XL")
            number = int(str(number)[1:])

    print("reduce_50", number, data)
    return number


def reduce_100(number, data):
    reminder = number // 100
    if reminder > 0:  # C
        if 400 > number >= 100:
            data.append("C" * int(str(number)[0]))
            number = int(str(number)[1:])
    print("reduce_100", number, data)
    return number


def reduce_500(number, data):
    reminder = number // 500
    if reminder > 0:  # D
        if 900 > number >= 500:
            data.append("D")
            number -= 500
    else:
        if 500 > number >= 400:
            data.append("CD")
            number = int(str(number)[1:])
    print("reduce_500", number, data)
    return number


def reduce_1000(number, data):
    reminder = number // 1000
    if reminder > 0:  # M
        number -= reminder * 1000
        data.append("M" * reminder)
    else:
        if number >= 900:
            data.append("CM")
            number -= 900
    print("reduce_1000", number, data)
    return number


def reduce(function, number, data, min, max):
    number = function(number, data)
    if max > number >= min:
            return function(number, data)
    return number


def checkio(number):

    data = []

    number = reduce(reduce_1000, number, data, 900, 1000)
    number = reduce(reduce_500, number, data, 500, 900)
    number = reduce(reduce_100, number, data, 100, 500)
    number = reduce(reduce_50, number, data, 50, 100)
    number = reduce(reduce_10, number, data, 10, 50)
    number = reduce_5(number, data)

    print(number, "".join(data))
    return "".join(data)

if __name__ == '__main__':


    assert checkio(1) == 'I', '1'
    assert checkio(2) == 'II', '2'
    assert checkio(3) == 'III', '3'
    assert checkio(4) == 'IV', '4'
    assert checkio(5) == 'V', '5'
    assert checkio(6) == 'VI', '6'
    assert checkio(7) == 'VII', '7'
    assert checkio(8) == 'VIII', '8'
    assert checkio(9) == 'IX', '9'
    assert checkio(10) == 'X', '10'
    assert checkio(11) == 'XI', '11'
    assert checkio(14) == 'XIV', '14'
    assert checkio(15) == 'XV', '15'
    assert checkio(18) == 'XVIII', '18'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(50) == "L", '50'
    assert checkio(53) == "LIII", '53'
    assert checkio(55) == "LV", '55'
    assert checkio(59) == "LIX", '59'
    assert checkio(60) == "LX", '60'
    assert checkio(65) == "LXV", '65'
    assert checkio(68) == "LXVIII", '68'
    assert checkio(69) == "LXIX", '69'
    assert checkio(100) == "C", '100'
    assert checkio(105) == "CV", '105'
    assert checkio(109) == "CIX", '109'
    assert checkio(300) == "CCC", '300'
    assert checkio(399) == "CCCXCIX", '399'
    assert checkio(400) == "CD", '400'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(500) == "D", "500"
    assert checkio(587) == "DLXXXVII", "587"
    assert checkio(1000) == "M", "1000"
    assert checkio(1001) == "MI", "1001"
    assert checkio(3000) == "MMM", "1000"
    assert checkio(2017) == "MMXVII", "2017"
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    assert checkio(3999) == 'MMMCMXCIX', '3999'
    assert checkio(44) == 'XLIV', '44'

