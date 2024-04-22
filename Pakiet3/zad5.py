import time

def generate_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fibGen = generate_fibonacci()
while True:
    print(next(fibGen))
    time.sleep(1)