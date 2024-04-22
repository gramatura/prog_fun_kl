def recursive_sum(liczby):
    suma = 0
    for element in liczby:
        if isinstance(element, list):
            suma += recursive_sum(element)
        else:
            suma += element
    return suma

liczby=[6,13,54]


print(recursive_sum(liczby))