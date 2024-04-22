from itertools import permutations

def penumeracje(lista):
    return list(permutations(lista))

lista = [1,2,3,4]
print(penumeracje(lista))