#include <iostream>
using namespace std;

int main() {
    long long int n;
    while (cin >> n) {
        int primers = 0;    // Comptem el nombre de primers d'un sol digit
        // Per a cada primer p d'un sol dígit...
        for (int p : {2, 3, 5, 7})    
            if (n % p == 0) {           // ...si p és divisor de n...
                ++primers;              // ...actualitzem el comptador
                while (n % p == 0)      // ...i eliminem p del producte de factors de n
                    n /= p;
            }
        
        // Si el nombre era xulo, haurem comptat 3 primers d'un sol dígit
        // i n valdrà 1
        cout << (primers == 3 and n == 1 ? "si" : "no") << endl;
    }
}