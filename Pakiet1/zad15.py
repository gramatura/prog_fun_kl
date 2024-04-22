def change(a):
    def add(b):
        print(a+b)
    return add

change(5)(10)
