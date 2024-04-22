def odliczanie(n):
    while n > 0:
        yield n
        n -= 1

licznik = odliczanie(5)
for numer in licznik:
    print(numer)