import math
import os

def clear():
    if os.name == 'posix':
        _ = os.system('clear')

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
                primes.append(int(i))
                pos = pos + 1

            primeNumber = primeNumber + 1

            if(pos == numOfPrimes):
                break

def findN(primes, numOfPrimes):
    aux = 1
    for i in range(numOfPrimes):
        aux *= primes[i]
    return int(aux)

def phiN(primes, numOfPrimes):
    aux = 1
    for i in range(numOfPrimes):
        aux *= (primes[i] - 1)
    return int(aux)

def findE(primes, numOfPrimes):
    count = 2
    while True:
        if(math.gcd(count, phiN(primes, numOfPrimes)) == 1):
            break
        else:
            count = count + 1
    return int(count)

def findInverseE(primes, numOfPrimes, e):
    return int(pow(int(e), -1, int(phiN(primes, numOfPrimes))))

def findD(primes, numOfPrimes, e):
    return int(findInverseE(primes, numOfPrimes, e) % phiN(primes, numOfPrimes))

def modularReduction(primes, reductions, d, numOfPrimes):
    for i in range(numOfPrimes):
        reductions.append(int(d % (primes[i] - 1)))

def findMis(primes, reductions, Mis, encrypt, numOfPrimes):
    for i in range(numOfPrimes):
        Mis.append(int(pow(encrypt, reductions[i]) % primes[i]))

def decrypt(primes, Mis, numOfPrimes,  n):
    result = 0
    N = []
    NLine = [] 
    for x in range(numOfPrimes):
        N.append(1)
        for y in range(numOfPrimes):
            N[x] *= primes[y]
        N[x] /= primes[x]
    for x in range(numOfPrimes):
        NLine.append(int(pow(int(N[x]), -1, int(primes[x]))))
    
    for i in range(numOfPrimes):
        result += Mis[i]*N[i]*NLine[i]

    return int(result % n)
