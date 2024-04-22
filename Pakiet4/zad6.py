def funkcja_do_listy(lista,funkcja):
    return [funkcja(element) for element in lista]

def dodawanie(element):
    return element + element

lista = [1,2,3,4,5]
n_lista = funkcja_do_listy(lista,dodawanie)
print(n_lista)