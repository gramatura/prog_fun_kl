def make_multiplier(x):

    def multipier(n):
        return x*n
    return multipier

double = make_multiplier(2)

print(double(5))