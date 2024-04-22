l = [(1,2,3,4), (3,4,5,6), (7,8,9,56,23,10),(9,10,11,12),(13,14,15,16)]
def custom_sort(l):
    l.sort(key = lambda x: (-x[1], -x[1]))
    return l
print(custom_sort(l))