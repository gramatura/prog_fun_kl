def composite(a,b):
    return lambda x : b(a(x))

def dodej(x):
    return x+2

def mno(x):
    return x*2

dodejpomnoz = composite(dodej,mno)
print (dodejpomnoz(5))