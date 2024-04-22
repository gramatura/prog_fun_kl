def slowa(string):
    slowo=""
    for x in string:
        if x == x.lower():
            slowo = slowo+x.upper()
        else:
            slowo = slowo+x.lower()
    return slowo

print(slowa("tOOtS"))