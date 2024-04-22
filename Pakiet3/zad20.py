def squareSum(n):
    suma=0
    for i in range(1, n + 1):
        suma +=(2*i-1)*(2*i-1)
    return suma

print(squareSum(8))