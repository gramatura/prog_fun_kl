def dziel_liste(lista,dlugosc):
    dzielone=[]
    for i in range(0,len(lista),dlugosc):
        dzielone.append(lista[i:i+dlugosc])
    return dzielone

lista = ["no","elo","mordo","co","tam","asd","asd","asdasdads","asdfggg",'asdasd']

print(dziel_liste(lista,3))