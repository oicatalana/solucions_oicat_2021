#include <iostream>
#include <random>
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

        // Assignem els colors aleatòriament fins trobar una manera bona
        VB color(n);		// color[k] és false si k és vermell, i true si és blau
        int total = m;		// Nombre d'arestes dolentes que hem comptat
        while (total > m/2) {
            // Tornem a començar. Marquem 0 arestes dolentes
            total = 0;

            // Pintem cada aresta vermella o blava amb probabilitat 0.5
            for (int i = 0; i < n; ++i)
                color[i] = rand()%2;

            // Comptem les arestes dolentes
            for (int i = 0; i < n; ++i)
                for (int j : G[i])
                    if (j < i and color[i] == color[j])
                        ++total;
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