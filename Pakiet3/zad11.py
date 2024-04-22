def find_max_min_diff(lista):
    max_value = max(lista)
    min_value = min(lista)
    diff = max_value - min_value
    return diff
lista = [1,2,3,4,5,6,7,8,9]
print(find_max_min_diff(lista))
