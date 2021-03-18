import math

def findPrimes(primes, numOfPrimes):

    primeNumber = 1
    pos = 0

    for i in range(2, 1001):

        divs = 0

        for j in range(2, i + 1):

            if(i % j == 0 and i != j):
                divs = divs + 1

        if(divs < 1):

            if(primeNumber > 1):
                primes.append(i)
                pos = pos + 1

            primeNumber = primeNumber + 1

            if(pos == numOfPrimes):
                break

def findN(primes, numOfPrimes):
    aux = 1
    for i in range(numOfPrimes):
        aux *= primes[i]
    return aux

def phiN(primes, numOfPrimes):
    aux = 1
    for i in range(numOfPrimes):
        aux *= (primes[i] - 1)
    return aux

def findE(primes, numOfPrimes):
    count = 2
    while True:
        if(math.gcd(count, phiN(primes, numOfPrimes)) == 1):
            break
        else:
            count = count + 1
    return count

def findInverseE(primes, numOfPrimes, e):
    count = 0
    while True:
        if((count * e) % phiN(primes, numOfPrimes) == 1):
            return count
        else:
            count = count + 1

def findD(primes, numOfPrimes, e):
    return findInverseE(primes, numOfPrimes, e) % phiN(primes, numOfPrimes)

def modularReduction(primes, reductions, d, numOfPrimes):
    for i in range(numOfPrimes):
        reductions.append(d % (primes[i] - 1))

def findMis(primes, reductions, Mis, encrypt, numOfPrimes):
    for i in range(numOfPrimes):
        Mis.append(pow(encrypt, reductions[i]) % primes[i])