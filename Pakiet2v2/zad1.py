from itertools import product

listaAB = ['A', 'B']
listaCD = ['C', 'D']

kombinacje = list(product(listaAB, listaCD))
print(kombinacje)