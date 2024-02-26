import time
def timeit(func):
    def costam():
        ts = time.perf_counter()
        func()
        te = time.perf_counter()
        print(f"czas: {te - ts} sekund")
    return costam
@timeit
def tw():
    sum([i**2 for i in range(10000000)])
tw()
