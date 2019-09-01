#include <iostream>
#include <cmath>

using namespace std;

long factorial(long n) {
    if(n == 0 || n == 1)
        return 1;
    else
        return ((n % long(pow(10, 9) + 7)) * (factorial(n-1)% long(pow(10, 9) + 7))) % long(pow(10, 9) + 7);
}

bool isPrime(int num) {
    for(int i = 2;i < num;++i) {
        if(num % i == 0)
            return false;
    }
    return true;
}

    int numPrimeArrangements(int n) {
        if(n == 1) return 1;
        if(n < 2) return 0;
        else if(n == 2) return 1;
        int count = 1;
        for(int i = 3;i <= n;++i) {
            if(isPrime(i)) {
                ++count;
            }
        }
        return long(factorial(count) * factorial(n - count)) % long(pow(10, 9) + 7);
    }

int main() {
    cout << numPrimeArrangements(100);
    return 0;
}
