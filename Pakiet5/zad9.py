from functools import reduce

cyfry = [3, 7, 2, 8, 5]
duza_liczba = reduce(lambda x, y: x if x > y else y, cyfry)

def srednia(cyfry):
    return reduce(lambda x, y: x + y, cyfry) / len(cyfry) if cyfry else 0

print(duza_liczba, srednia(cyfry))