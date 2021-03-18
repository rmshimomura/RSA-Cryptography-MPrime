#include <math.h>
#include <stdio.h>
#include <stdlib.h>

int gcd(int a, int b){ 
    //Greatest common divisor
    int result = 1;
    int tempA = a;
    int tempB = b;
    for(int i = 2; i < 1000; i++){
    int divs = 0;
        for(int j = 2; j < i; j++){
            if(i % j == 0 && i != j){
                divs++;
            }
        }
        if(divs < 1){
            if(tempA % i == 0 && tempB % i == 0){
                tempA /= i;
                tempB /= i;
                result *= i;
                i--;
                
            }
        }
    }
    return result;
}

long int myPower(long int base, long int exponent) { 
    //My power replaces pow from math.h because of some problem with modulo operation
    long int result = 1;
    for (int i = 0; i < exponent; i++) {
        result *= base;
    }
    return result;
}

void findPrimes(long int* vectorOfPrimes, int numOfPrimes) {
    //Find primes for encryption 
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
    //The first part of the public key that is the product of the primes
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

long int findE(long int* vectorOfPrimes, int numOfPrimes){
    //Find e, following the rules of the GDC between e and phiN needs to be 1
    //Using brute force to find the smaller e that satisfies the requirements
    int count = 2;
    while(1){
        if(gcd(count, phiN(vectorOfPrimes, numOfPrimes)) == 1){
            break;
        }else{
            count++;
        }
    }
    return count;
}

long int findPrivateKey(long int* vectorOfPrimes, int numOfPrimes, int e){
    return findInverseE(vectorOfPrimes, 3, e) % phiN(vectorOfPrimes, numOfPrimes);
}


int main() {
    long int v[3];
    long int M = 123;
    findPrimes(v, 3);
    long int publicKey = findPublicKey(v,3);
    long int e = findE(v, 3);
    long int inversee = findInverseE(v,3,e);
    long int privateKey = findPrivateKey(v,3,e);
    printf("e = %ld inverse = %ld privatekey = %ld \n", e, inversee, privateKey);
    printf("result enc = %ld\n", myPower(M, e) % publicKey);
}