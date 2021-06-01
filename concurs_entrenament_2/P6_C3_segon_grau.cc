#include <iostream>
#include <cmath>
using namespace std;

int main() {
    long long int n;
    while (cin >> n)
        cout << int((-1 + sqrt(1 + 8*n))/2) << endl;
}

