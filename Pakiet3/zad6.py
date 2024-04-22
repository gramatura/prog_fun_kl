def map_nested(func, gniazdowa_lista):
    return [map_nested(func, sublist) if isinstance(sublist, list) else func(sublist) for sublist in gniazdowa_lista]

def square(x):
    return x ** 2

gniazdowa_lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

mapped_list = map_nested(square, gniazdowa_lista)

print(mapped_list)