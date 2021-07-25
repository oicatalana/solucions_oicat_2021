#include <iostream>
using namespace std;

int s(int n) {
    if (n < 10)
        return n;
    return s(n/10) + (n%10);
}

int p(int n) {
    if (n < 10)
        return n;
    return p(n/10) * (n%10);
}

int main() {
    int suma_peculiars = 0;
    for (int n = 1; n <= 1000000; ++n)
        if (n == s(n) + p(n)) {
            suma_peculiars += n;
            cout << "Nombre peculiar trobat: " << n << endl;
        }
    cout << "SUMA: " << suma_peculiars << endl;
}