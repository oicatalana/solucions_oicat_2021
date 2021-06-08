#include <iostream>
using namespace std;

typedef long long int LL;

LL resol(LL n) {
    if (n == 0)
        return 0;

    // Trobem el major 2^m tal que 2^m <= n, i calculem 3^m
    LL pot_2 = 1, pot_3 = 1;
    while (2*pot_2 <= n) {
        pot_2 *= 2;
        pot_3 *= 3;
    }

    // La resposta serà resol(n) = resol(2^m) + 2*resol(n - 2^m).
    // Tenint en compte que resol(2^m) = 3^m:
    return pot_3 + 2*resol(n - pot_2);
}

int main(){
    LL k, n;
    while (cin >> k >> n) 
        cout << (k%2 == 0 ? 0 : resol(n)) << endl;
}