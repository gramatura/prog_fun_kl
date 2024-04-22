slowa = ['arbuz','ajapko','amalina','niemalina','nieporzeczka']
a_slowa = list(filter(lambda word: word.startswith('a'), slowa))

numery = [1, 2, 3, 4, 5]
kwadraty = list(map(lambda x: x ** 2, numery))

print(a_slowa,kwadraty)