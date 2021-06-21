#include <iostream>
#include <map>
using namespace std;

int main() {
    map<int, int> M;    // M[x]: quantitat de productes amb preu x

    char c;
    while (cin >> c) {
        if (c == 'N') {
            if (M.empty())  // Si M està buit, imprimim missatge d'error
                cout << "error: magatzem buit" << endl;
            else            // Escrivim el preu més baix
                cout << M.begin()->first << endl;
        }
        if (c == 'X') {
            if (M.empty())  // Si M està buit, imprimim missatge d'error
                cout << "error: magatzem buit" << endl;
            else {          // Escrivim el preu més alt
                auto it = M.end();
                --it;
                cout << it->first << endl;
            }
        }
        if (c == 'A') {
            int x;
            cin >> x;
            ++M[x];         // Augmentem M[x] en 1
        }
        if (c == 'M') {
            int x;
            cin >> x;
            if (M.count(x) == 0)    // Si M no conté x, imprimim missatge d'error
                cout << "error: preu inexistent (" << x << ')' << endl;
            else if (M[x] == 1)     // Si només queda un producte amb preu x, borrem x de M
                M.erase(x);
            else                    // Restem 1 a M[x]
                --M[x];
        }
    }
}