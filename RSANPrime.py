import math

def encontrarN(primes, nOP):
    aux = 1
    for i in range(nOP):
        aux *= primes[i]
    return aux


def phiN(primes, nOP):
    aux = 1
    for i in range(nOP):
        aux *= (primes[i] - 1)
    return aux


def encontrarE(primes, nOP):
    count = 2
    while True:
        if(math.gcd(count, phiN(primes, nOP)) == 1):
            break
        else:
            count = count + 1
    return count


def encontrarInversoE(primes, nOP, e):
    return pow(int(e), -1, int(phiN(primes, nOP)))


def encontrarD(primes, nOP, e):
    return int(encontrarInversoE(primes, nOP, e) % phiN(primes, nOP))


def reducaoModular(primes, reductions, d, nOP):
    for i in range(nOP):
        reductions.append(int(d % (primes[i] - 1)))


def encontrarMis(primes, reductions, Mis, encrypt, nOP):
    for i in range(nOP):
        Mis.append(int(pow(encrypt, reductions[i], primes[i])))


def encrypt(M, e, n):
    return int(pow(M, e, n))


def decrypt(primes, Mis, nOP,  n):
    result = 0
    N = []
    NLine = []

    for x in range(nOP):
        N.append(1)
        for y in range(nOP):
            if x != y:
                N[x] *= int(primes[y])

    for x in range(nOP):
        NLine.append(int(pow(N[x], -1, primes[x])))

    for i in range(nOP):
        result += (Mis[i]*N[i]*NLine[i])

    return int(result % n)
