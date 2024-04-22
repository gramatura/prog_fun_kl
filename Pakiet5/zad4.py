def dodejfunkcje(func, x, y):
    return func(x, y)

def osiem(x,y):
    if(x == 8 & y == 8):
        return x,y
    else:
        return print("sory to nie osiem")
##tak wiem że ta funkcja nie ma żadnego sensu
##zrobiona jest tresc zadadania xd

print(dodejfunkcje(osiem, 8, 8))