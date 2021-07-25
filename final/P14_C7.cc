#include <iostream>
#include <utility>
#include <vector>
using namespace std;

typedef vector<bool> VB;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

int main() {
    int n, m;
    while (cin >> n >> m) {
        // Llegim el graf
        VVI G(n);
        for (int i = 0; i < m; ++i) {
            int a, b;
            cin >> a >> b;
            G[a].push_back(b);
            G[b].push_back(a);
        }

        // Assignem els colors
        VB color(n);		// color[k] és false si k és vermell, i true si és blau
        int total = 0;		// Nombre d'arestes dolentes que hem comptat
        for (int i = 0; i < n; ++i) {
            // Comptem quants veïns de cada color j, amb j < i, té i 
            int vermells = 0;
            int blaus = 0;
            for (int j : G[i])
                if (j < i) {
                    if (color[j])
                        ++blaus;
                    else
                        ++vermells;
                }

            // Pintem i del color corresponent
            if (blaus > vermells) {
                color[i] = false;
                total += vermells;
            }
            else {
                color[i] = true;
                total += blaus;
            }
        }

        // Escrivim la resposta
        cout << total;
        for (int i = 0; i < n; ++i)
            for (int j : G[i])
                if (j < i and color[i] == color[j])
                    cout << "  " << i << ' ' << j;
        cout << endl;
    }
}