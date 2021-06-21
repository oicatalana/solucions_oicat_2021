#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        // Si a la nostra llista li afegim 3 zeros al principi,
        // el resultat serà al mateix, i els càlculs es simplificaran
        int m = n + 3;                  // Longitud de la llista ampliada
        vector<long long int> v(m, 0);  // v[i]: i-èssim element de la llista ampliada            
        vector<long long int> dp(m, 0); // dp[i]: Màxim resultat fins l'i-èssim element

        // Llegim cada nombre, i actualitzem el màxim
        for (int i = 3; i < m; ++i) {
            cin >> v[i];
            dp[i] = max({
                dp[i - 1] + v[i], 
                dp[i - 2] + v[i - 1]*v[i], 
                dp[i - 3] + v[i - 2]*v[i - 1]*v[i]
            });
        }

        // El nostre resultat serà dp[m - 1], el màxim agafant tots els elements
        cout << dp[m - 1] << endl;
    }
}