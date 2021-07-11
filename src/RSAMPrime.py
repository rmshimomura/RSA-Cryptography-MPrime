import math

def find_N(primes, number_of_primes):
    aux = 1
    for i in range(number_of_primes):
        aux *= primes[i]
    return aux


def phi_N(primes, number_of_primes):
    aux = 1
    for i in range(number_of_primes):
        aux *= (primes[i] - 1)
    return aux


def find_E(primes, number_of_primes):
    count = 2
    while True:
        if(math.gcd(count, phi_N(primes, number_of_primes)) == 1):
            break
        else:
            count = count + 1
    return count


def find_inverse_E(primes, number_of_primes, e):
    return pow(int(e), -1, int(phi_N(primes, number_of_primes)))


def find_D(primes, number_of_primes, e):
    return int(find_inverse_E(primes, number_of_primes, e) % phi_N(primes, number_of_primes))


def modular_reduction(primes, reductions, d, number_of_primes):
    for i in range(number_of_primes):
        reductions.append(int(d % (primes[i] - 1)))


def find_Mis(primes, reductions, mis, encrypt, number_of_primes):
    for i in range(number_of_primes):
        mis.append(int(pow(encrypt, reductions[i], primes[i])))


def encrypt(M, e, n):
    return int(pow(M, e, n))


def decrypt(primes, mis, number_of_primes,  n):
    result = 0
    N = []
    N_line = []

    for x in range(number_of_primes):
        N.append(1)
        for y in range(number_of_primes):
            if x != y:
                N[x] *= int(primes[y])

    for x in range(number_of_primes):
        N_line.append(int(pow(N[x], -1, primes[x])))

    for i in range(number_of_primes):
        result += (mis[i]*N[i]*N_line[i])

    return int(result % n)
