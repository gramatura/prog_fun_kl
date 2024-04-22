def analyze_data(data):
    match data:
        case tuple():
            return f'Masz tu Tuple z {len(data)} ylementami'
        case list():
            return f'Masz tu Liste z {len(data)} ylementami'

print(analyze_data([]))
print(analyze_data([1]))
print(analyze_data([1, 2, 3]))
print(analyze_data((1, 2)))
print(analyze_data((1, 2, 3, 4)))
print(analyze_data({"key": "value"}))