def safe_function(func):
    def dekorator(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Ale erorra walneło: {e}")
            return None
    return dekorator

@safe_function
def divide(x, y):
    return x / y

print(divide(10, 0))
print(divide(21,37))