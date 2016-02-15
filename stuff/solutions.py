def exc_lists():
    """
    Create following lists:

    - List A: numbers from 0 to 100, hint: help(range)
    - List B: only even numbers from list A
    - List C: numbers from list A sorted in descent order
    - List D: all numbers from list B should be squared (number ^ 2)
    - List E: only numbers from 20 to 60 from list A
    - List F: only numbers from 100 to 70 from list A
    - List G: sum of list E and F
    - List H: list G plus number 1000
    - List I: copy of list H
    - List J: from list H remove smallest number
    - List K: list H extended with list ['A', 'B', 'C']

    Create following variables:
    - v1: sum of numbers from list B
    - v2: maximum number from list H
    - v3: minimum number from list H
    - v4: average number from list G

    """

    #List A: numbers from 0 to 100, hint: help(range)
    A = list(range(0, 101))

    #List B: only even numbers from list A
    #B = list(range(0, 100, 2))
    B = [number for number in range(0, 101) if number % 2 == 0]

    #List C: numbers from list A sorted in descent order
    C = sorted(B, reverse=True)

    #List D: all numbers from list B should be squared (number ^ 2)
    D = [pow(number, 2) for number in B]

    #List E: only numbers from 20 to 60 from list A
    E = A[20:60]

    #List F: only numbers from 100 to 70 from list A
    F = list(reversed(A[70:101]))
    #F = A[100:70:-1]

    #List G: sum of list E and F
    G = E + F

    #List H: list G plus number 1000
    H = G.copy()
    H.append(1000)

    #List I: copy of list H
    I = H.copy()

    #List J: from list H remove smallest number
    J = H.copy()
    J.remove(min(J))

    #List K: list H extended with list ['A', 'B', 'C']
    K = H.copy()
    K.extend(['A', 'B', 'C'])

    print(A)
    print(B)
    print(C)
    print(D)
    print(E)
    print(F)
    print(G)
    print(H)
    print(I)
    print(J)
    print(K)

    # v1: sum of numbers from list B

    v1 = sum(B)
    print(v1)
    # v2: maximum number from list H
    # v3: minimum number from list H
    # v4: average number from list G
    print(sum(G)/len(G))


def exc_dictionaries():
    """
    Create three dictionaries that will contain following information from premier league table:

    postion, club, played, won, drawn, lost, points
    1	Leicester City	    25	15	8	2	53
    2   Tottenham Hotspur	25	13	9	3	48
    3	Arsenal	            25	14	6	5	48

    1) print each dictionary in given order as you have in premier league table: postion, club, played, won, drawn, lost, points
    expected output:
    1 - Leicester City - 25 - 15 - 8 - 2 - 53
    2 - Tottenham Hotspur - 25 - 13 - 9 - 3 - 48
    3 - Arsenal	- 25 - 14 - 6 - 5 - 48

    2) create list PREMIER_LEAGUE_POINTS and put these three dictionaries inside this list
    and then sort by club points (Leicester should be first on this list)

    """

    leicester = {'club': 'Leicester City', 'position': 1, 'played': 25, 'won': 15, 'drawn': 15, 'lost': 2, 'points': 53}
    totenham = {'club': 'Toteham Hotspur', 'position': 2, 'played': 25, 'won': 13, 'drawn': 9, 'lost': 3, 'points': 48}
    arsenal = {'club': 'Arsenal', 'position': 2, 'played': 25, 'won': 14, 'drawn': 6, 'lost': 5, 'points': 48}

    to_print = "{d[position]} - {d[club]} - {d[played]} - {d[won]} - {d[drawn]} - {d[lost]} - {d[points]}"
    print(to_print.format(d=leicester))
    print(to_print.format(d=totenham))
    print(to_print.format(d=arsenal))

    PREMIER_LEAGUE_POINTS = [leicester, totenham, arsenal]

    print(PREMIER_LEAGUE_POINTS)

    # from PREMIER_LEAGUE_POINTS select clubs with losts number not higher than 3 (lost <= 3) and print its names

    for club in PREMIER_LEAGUE_POINTS:
        if club['lost'] >= 3:
            print(club['club'])

    # create new list of dictionaries CLUB_POINTS from PREMIER_LEAGUE_POINTS, new dictionary should contain only club name and points number

    CLUB_POINTS = []
    for club in PREMIER_LEAGUE_POINTS:
        new_dict = {club['club']: club['points']}
        CLUB_POINTS.append(new_dict)
    print(CLUB_POINTS)


def tax_price_calculator(price, tax=0.24):
    return price + (price * tax)


def exc_functions_1():

    print(tax_price_calculator(30))
    print(tax_price_calculator(30, tax=2))


import string
import random
def generate_password(length):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    password_chars = []
    password_chars.extend(letters)
    password_chars.extend(digits)
    password_chars.extend(special)

    print(password_chars)

    return ''.join(random.choice(password_chars) for _ in range(length))


def exc_functions_2():
    """
    Create function that will generate random string (pseudo password) of size N.
    Our password should contains upper and lower letters + digits + special characters (only . , : are allowed)

    """

    password = generate_password(50)

    print(password)



def exc_files():

    # 1. create random.dat file - to file insert random string of size 512 characters

    with open('random.dat', 'w') as f:
        f.write(generate_password(512))

    with open('random.dat', 'r') as f:
        content = f.read()

    LETTERS_LIST = []
    NUMBERS_LIST = []
    for line in content:
        for char in line:
            if char in list(string.ascii_letters):
                LETTERS_LIST.append(char)
            if char in list(string.digits):
                NUMBERS_LIST.append(char)

    print(LETTERS_LIST)
    print(NUMBERS_LIST)

    # create unique_data.dat file that will contain unique data from random.dat file

    with open('unique.dat', 'w') as f:
        f.write(''.join(set(sorted(content))))


exc_lists()
exc_dictionaries()
exc_functions_1()
exc_functions_2()
exc_files()