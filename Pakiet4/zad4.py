def gen_pot(exponent):
    def pot(x):
        return x**exponent
    return pot

pot = gen_pot(2)
wynik = pot(6)

print(wynik)