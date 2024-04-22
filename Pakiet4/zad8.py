from typing import Counter

def naj_wys_el(lista):
    licznik= Counter(lista)
    naj_wys = licznik.most_common(1)[0][0]
    return naj_wys

lista = [1,1,1,2,2,2,2,3,3,3,3,3,"red","red","red","red","red"]
print(naj_wys_el(lista))