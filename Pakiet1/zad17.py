from functools import partial

def dodejpinc(x):
    return x+5

dodej5 = partial(dodejpinc)

print(dodej5(6))