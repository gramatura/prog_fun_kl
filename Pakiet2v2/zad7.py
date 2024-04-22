from itertools import groupby

numery = [1, 2, 3, 4, 5, 6, 7, 8, 9]

grupowanie = {is_even: [x for x in group] for is_even, group in groupby(numery, key=lambda x: x % 2 == 0)}
print(grupowanie)