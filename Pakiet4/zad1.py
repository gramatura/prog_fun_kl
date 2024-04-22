def suma_p(lista):
    suma=0
    for liczba in lista:
        if liczba % 2 == 0:
            suma = suma+liczba
    return suma

print(suma_p([1,2,3,4,5,6,7,8,9,10]))