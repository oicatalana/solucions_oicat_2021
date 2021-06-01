#include <bits/stdc++.h>
using namespace std;

int main() {
    string s;
    while (cin >> s) {
        int n = s.size();

        // Comencem amb un "le", seguit d'un espai
        cout << "le ";

        // Canviem "oi"s per "ua"s
        for (int i = 1; i < n; ++i)
            if (s[i - 1] == 'o' and s[i] == 'i') {
                s[i - 1] = 'u';
                s[i] = 'a';
            }

        // Canviem "nt" al final per "ng"
        if (n > 1 and s[n - 2] == 'n' and s[n - 1] == 't')
            s[n - 1] = 'g';

        // Escrivim la paraula. A cada 'r' que trobem, afegim una 'g'
        for (int i = 0; i < n; ++i) {
            cout << s[i];
            if (s[i] == 'r')
                cout << 'g';
        }

        cout << endl;
    }
}