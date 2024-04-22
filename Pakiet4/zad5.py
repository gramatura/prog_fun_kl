def dziel_liste(lista,max_dlugosc):
    dzielone=[]
    for i in range(0,len(lista),max_dlugosc):
        dzielone.append(lista[i:i+max_dlugosc])
    return dzielone

lista = ["no","elo","mordo","co","tam"]

print(dziel_liste(lista,3))