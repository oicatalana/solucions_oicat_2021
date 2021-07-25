#include <iostream>
#include <vector>
using namespace std;

// ASSUMIM QUE A[i] < i!!!!!

int main() {
    int n;
    while (cin >> n) {
        // Llegim la llista
        vector<int> A(n);
        for (int& x : A)
            cin >> x;

        // L'última posició sempre és perdedora. Mirant de dreta a esquerra,
        // si la nostra posició j és perdedora, llavors A[j] és guanyadora
        vector<bool> es_posicio_guanyadora(n, false);
        for (int j = n - 1; j > 0; --j)
            if (!es_posicio_guanyadora[j])
                es_posicio_guanyadora[A[j]] = true;

        // Responem en funció de si la primera posició és guanyadora
        cout << (es_posicio_guanyadora[0] ? "Max" : "Izan") << endl;
    }
}