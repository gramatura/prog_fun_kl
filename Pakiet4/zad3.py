def filtruj_slownik(slownik):
    n_slownik={}
    for key,value in slownik.items():
        if isinstance(value,int) and value % 2 == 0:
            n_slownik[key]=value
    return n_slownik

slownik = {"a":1,"b":2,"c":3,"d":4}

print(filtruj_slownik(slownik))