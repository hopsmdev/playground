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

roman_map = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
             ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
             ('V', 5), ('IV', 4), ('I', 1)]


def checkio(data):
    roman_numbers = []
    for roman_letter, number in roman_map:
        while number <= data:
            roman_numbers.append(roman_letter)
            data -= number
            if data == 0:
                return "".join(roman_numbers)


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