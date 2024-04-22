def kwadrat(x):
    return x ** 2

def dej_piec(x):
    return x + 5

def dodej_funkcje(y):
    return list(map(lambda x: dej_piec(kwadrat(x)), y))

y = [1, 2, 3, 4, 5]
print(dodej_funkcje(y))