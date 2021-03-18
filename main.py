from functions import *
numero_de_primos = int(input("quantos primos? "))
primos = []
reductions = []
Mis = []
M = 75
findPrimes(primos, numero_de_primos)
n = findN(primos, numero_de_primos)
e = findE(primos, numero_de_primos)
inverse = findInverseE(primos, numero_de_primos, e)
d = findD(primos, numero_de_primos, e)
phi = phiN(primos, numero_de_primos)
encrypt = pow(M, e) % n
modularReduction(primos, reductions, d, numero_de_primos)
findMis(primos, reductions, Mis, encrypt, numero_de_primos)
# print(f"M = {M} n = {n} e = {e} inverse = {inverse} d = {d} phiN = {phi} encrypt = {encrypt}")
for x in range(numero_de_primos):
    print(f"primos[{x}] = {primos[x]}")
print("========")
for x in range(numero_de_primos):
    print(f"reductions[{x}] = {reductions[x]}")
print("========")
for x in range(numero_de_primos):
    print(f"Mis[{x}] = {Mis[x]}")