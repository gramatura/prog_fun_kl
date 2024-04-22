def lacz_slownik(*slowniki):
    polaczany_slownik={}
    for slownik in slowniki:
        for key,value in slownik.items():
            if key in polaczany_slownik:
                polaczany_slownik[key] += value
            else:
                polaczany_slownik[key] = value
    return polaczany_slownik

s1={"a":1,"b":2,"c":3}
s2={"b":4,"e":5,"f":6}
s3={"g":7,"f":8,"i":9}

polaczany_slownik=lacz_slownik(s1,s2,s3)
print(polaczany_slownik)