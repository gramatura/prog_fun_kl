def fibonaci(n):
    if n <= 1:
        return n
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)
pirwsze10 = [fibonaci(i) for i in range(10)]
print(pirwsze10)