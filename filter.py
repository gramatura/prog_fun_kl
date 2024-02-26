slowa = ["Eee", "Eeee", "Eeeee","Eeeeee"]
print(slowa)

def wincyj_niz_5(slowa):
    return len(slowa) > 5

dlugie_slowa = list(filter(wincyj_niz_5, slowa))
print (dlugie_slowa)