#include <math.h>
#include <stdio.h>
#include <stdlib.h>

long int myPower(long int base, long int exponent) {
    long int result = 1;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}

void findPrimes(long int* vectorOfPrimes, int numOfPrimes) {
    int pos = 0;
    int primeNumber = 1;
    for (int i = 2; i < 1000; i++) {
        int divs = 0;
        for (int j = 2; j < i; j++) {
            if (i % j == 0 && i != j) {
                divs++;
            }
        }
        if (divs < 1) {
            if(primeNumber > 1){
                vectorOfPrimes[pos++] = i;
            }
            primeNumber++;
            if (pos == numOfPrimes) {
                break;
            }
        }
    }
}

long int findPublicKey(long int* vectorOfPrimes, int numOfPrimes) {
    long int N = 1;
    for (int i = 0; i < numOfPrimes; i++) {
        N *= vectorOfPrimes[i];
    }
    return N;
}

long int phiN(long int* vectorOfPrimes, int numOfPrimes) {
    long int aux = 1;
    for (int i = 0; i < numOfPrimes; i++) {
        aux *= (vectorOfPrimes[i] - 1);
    }
    return aux;
}

long int findInverseE(long int* vectorOfPrimes, int numOfPrimes, int e){
    int count = 0;
    //Inverse E in this case is the number that multiplied by "e" module phiN == 1
    while(1){
        if((count*e) % phiN(vectorOfPrimes, numOfPrimes) == 1){
            return count;
        }else{
            count++;
        }
    }
}

long int findPrivateKey(long int* vectorOfPrimes, int numOfPrimes, int e){
    return findInverseE(vectorOfPrimes, 3, e) % phiN(vectorOfPrimes, numOfPrimes);
}


int main() {
    long int v[3];
    long int M = 75;
    findPrimes(v, 3);
    long int publicKey = findPublicKey(v,3);
    long int e = 5;
    long int inversee = findInverseE(v,3,e);
    long int privateKey = findPrivateKey(v,3,e);

    printf("result enc = %ld\n", myPower(M, e) % publicKey);
}