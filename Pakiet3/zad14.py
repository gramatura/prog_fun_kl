lista=[1,1,1,2,2,2,3,3,3,]

def count_unique_elements(lista):
    unique_set=set(lista)
    unique_count=len(unique_set)
    return unique_count

print(count_unique_elements(lista))