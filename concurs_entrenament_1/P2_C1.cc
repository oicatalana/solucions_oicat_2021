#include <iostream>
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        int suma = 0;
        for (int i = 1; i <= n; ++i)
            suma = suma + i*i;
        cout << suma << endl;
    }
} 