from itertools import combinations

def generetejszynofkombinejszyn(elementejszyn):
    return list(combinations(elementejszyn, 2))

elementejszyn = [8, 16, 32, 64]
print(generetejszynofkombinejszyn(elementejszyn))