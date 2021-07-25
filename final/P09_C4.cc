#include <iostream>
#include <vector>
using namespace std;

int main() {
    string s;
    while (cin >> s) {
        // Busquem totes les posicions dolentes (i's tal que s[i] != s[n - i - 1])
        vector<int> posicions_dolentes;
        int n = s.size();
        for (int i = 0; i < n - i - 1; ++i)
            if (s[i] != s[n - i - 1])
                posicions_dolentes.push_back(i);

        // Si no n'hi ha cap, és palíndrom de longitud >= 2, i per tant quasipalíndrom
        if (posicions_dolentes.size() == 0)
            cout << "SI" << endl;
        // Si hi ha una posició dolenta a, intentem intercanviar
        // o bé a, o bé n - a - 1 per l'element del mig
        else if (posicions_dolentes.size() == 1) {
            int a = posicions_dolentes[0];
            if (n%2 == 1 and (s[n/2] == s[a] or s[n/2] == s[n - a - 1]))
                cout << "SI" << endl;
            else
                cout << "NO" << endl;
        }
        // Si hi ha dues posicions dolentes a i b, intentem fer un intercanvi
        // entre un element del parell (s[a], s[n - a - 1]) i un de (s[b], s[n - b - 1])
        else if (posicions_dolentes.size() == 2) {
            char x = s[posicions_dolentes[0]];
            char X = s[n - posicions_dolentes[0] - 1];
            char y = s[posicions_dolentes[1]];
            char Y = s[n - posicions_dolentes[1] - 1];
            // Podem comprovar que els dos parells tenen els mateixos elements d'aquesta manera
            if (min(x, X) == min(y, Y) and max(x, X) == max(y, Y))
                cout << "SI" << endl;
            else
                cout << "NO" << endl;
        }
        // Si hi ha >= 3 dolentes, no pot ser quasipalíndrom
        else
            cout << "NO" << endl;
    }
}