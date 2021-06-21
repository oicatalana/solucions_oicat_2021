#include <iostream>
#include <set>
using namespace std;

int main() {
    multiset<int> M;        // Preus dels productes guardats

    char c;
    while (cin >> c) {
        if (c == 'N') {
            if (M.empty())  // Si M està buit, imprimim missatge d'error
                cout << "error: magatzem buit" << endl;
            else            // Escrivim el preu més baix
                cout << *M.begin() << endl;
        }
        if (c == 'X') {
            if (M.empty())  // Si M està buit, imprimim missatge d'error
                cout << "error: magatzem buit" << endl;
            else {          // Escrivim el preu més alt
                auto it = M.end();
                --it;
                cout << *it << endl;
            }
        }
        if (c == 'A') {
            int x;
            cin >> x;
            M.insert(x);    // Afegim x a M
        }
        if (c == 'M') {
            int x;
            cin >> x;
            if (M.count(x) == 0)    // Si M no conté x, imprimim missatge d'error    
                cout << "error: preu inexistent (" << x << ')' << endl;
            else        // Borrem una sola còpia de x (M.erase(x) ens les borraria totes)
                M.erase(M.find(x));
        }
    }
}