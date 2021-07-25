#include <iostream>
#include <vector>
using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;

int main() {
    int n, m;
    while (cin >> n >> m) {
        // Llegim la matriu
        VVI A(n, VI(m));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                cin >> A[i][j];

        // Llista de cantonades, i la variable on guardarem la solució
        VPII cantonades = {{0, 0}, {n - 1, 0}, {0, m - 1}, {n - 1, m - 1}};
        int sol = -1;

        // Comparem cada element de la matriu amb els elements de les cantonades.
        // Si són diferents, actualitzem la solució
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
                for (PII c : cantonades)
                    if (A[i][j] != A[c.first][c.second])
                        sol = max(sol, abs(c.first - i) + abs(c.second - j));

        // Imprimim la solució
        cout << sol << endl;
    }
}