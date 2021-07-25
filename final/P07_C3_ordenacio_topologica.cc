#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int n;
	while (cin >> n) {
        // Llegim la llista
		vector<int> A(n);
        for (int& x : A)
            cin >> x;

        // outdegree[j] ens diu quants i compleixen A[i] = j
        vector<int> outdegree(n, 0);
        for (int j = 1; j < n; ++j)
            ++outdegree[A[j]];

        // Per a cada posició, ens guardem si és guanyadora
        vector<bool> es_posicio_guanyadora(n, false);

        // Llista de posicions per a les quals ja sabem si són o no guanyadores
        // Inicialment, seran les posicions per a les quals no es pot seguir avançant
        queue<int> posicions_conegudes;
        for (int i = 0; i < n; ++i)
            if (outdegree[i] == 0)
                posicions_conegudes.push(i);

        // Per a cada posició coneguda j, actualitzem la posició i = a_j
        // outdegree[i] ara calcularà a quantes posicions j podem anar des de i
        // per a les quals encara no hem calculat totalment si j és guanyadora
        while (posicions_conegudes.front() != 0) {
            int j = posicions_conegudes.front();
            int i = A[j];
            posicions_conegudes.pop();

            if (!es_posicio_guanyadora[j])
                es_posicio_guanyadora[i] = true;

            outdegree[i] -= 1;
            if (outdegree[i] == 0)
                posicions_conegudes.push(i);
        }
    	
        // Responem en funció de si la primera posició és guanyadora
		cout << (es_posicio_guanyadora[0] ? "Max" : "Izan") << endl;
    }
}
