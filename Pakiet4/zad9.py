def funkcja_do_krotki(lista_krotek,funkcja):
    return [funkcja(krotka) for krotka in lista_krotek]

def suma_krotek(krotka):
    return sum(krotka)

lista_krotek = [(1,2),(3,4),(5,6)]
n_lista = funkcja_do_krotki(lista_krotek,suma_krotek)
print(n_lista)