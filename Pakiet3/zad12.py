def rotate (l,n):
    return l[n:] + l[:n]

lista =[1,2,3,4]
print(rotate(lista, 2))