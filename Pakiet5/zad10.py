def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def duzy_plik(sciezka):
    with open(sciezka, 'r') as file:
        for line in file:
            yield line.strip()

sciezka = 'large_file.txt'
linie = duzy_plik(sciezka)
for _ in range(5):
    print(next(linie))