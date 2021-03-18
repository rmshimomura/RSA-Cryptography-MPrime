from functions import *
numberOfPrimes = int(input("For this encryption, how many primes would you like to use ? "))
case = int(input("Would you like to insert the primes that will be used? : (0 for no | 1 for yes)"))
clear()
primes = []
reductions = []
Mis = []
if(case == 0):
    findPrimes(primes, numberOfPrimes)
else:
    for i in range(numberOfPrimes):
        primes.append(int(input(f"Insira o primo {i + 1} : ")))

M = int(input("Which message do you like to send? "))
n = findN(primes, numberOfPrimes)
e = findE(primes, numberOfPrimes)
inverse = findInverseE(primes, numberOfPrimes, e)
d = findD(primes, numberOfPrimes, e)
phi = phiN(primes, numberOfPrimes)
print(f"M = {M} n = {n} e = {e} inverse = {inverse} d = {d} phiN = {phi}")
encrypt = pow(M, e) % n
modularReduction(primes, reductions, d, numberOfPrimes)
findMis(primes, reductions, Mis, encrypt, numberOfPrimes)
decryptResult = decrypt(primes, Mis, numberOfPrimes, n)

# for x in range(numberOfPrimes):
#     print(f"primes[{x}] = {primes[x]}")
# print("========")
# for x in range(numberOfPrimes):
#     print(f"reductions[{x}] = {reductions[x]}")
# print("========")
# for x in range(numberOfPrimes):
#     print(f"Mis[{x}] = {Mis[x]}")
print("========")
print(f"encrypt = {encrypt}")
print(f"decrypt = {decryptResult}")