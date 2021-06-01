#include <iostream>
#include <cmath>
using namespace std;

int main() {
    long long int n;
    while (cin >> n) {
        long long int y = int(sqrt(2*n));
        if (y*(y + 1)/2 <= n)
            cout << y << endl;
        else
            cout << y - 1 << endl;
    }
}

