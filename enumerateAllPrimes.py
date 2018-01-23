def countPrimes(n):
    if n < 3:
        return 0
    primes = [True] * n
    indexes = []
    primes[0] = primes[1] = False
    for i in range(2, n):
        if primes[i] == True:
           for j in range(2, (n-1)//i+1):
               primes[i*j] = False
    #return primes
    for x in range(0,len(primes)):
        if primes[x] == True:
            indexes.append(x)
    return indexes

n = 10
print countPrimes(n)