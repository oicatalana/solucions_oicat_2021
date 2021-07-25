#include <iostream>
#include <vector>
using namespace std;

// T[i]: llista de posicions on podem anar des de la posició i
vector<vector<int>> T;

// Una posició és perdedora si no es pot avançar a cap altre posició,
// o si totes les posicions a les que es pot avançar són guanyadores
// (cosa que vol dir que l'altre jugador guanya)
bool es_posicio_guanyadora(int i) {
	for (int j : T[i])
		if (!es_posicio_guanyadora(j))
			return true;
	return false;
}

int main() {
	int n;
	while (cin >> n) {
		// Reiniciem T
		T = vector<vector<int>>(n);

		// Construïm T mentre anem llegint l'entrada. 
		for (int j = 0; j < n; ++j) {
			int i;
			cin >> i;
			if (j > 0)
				T[i].push_back(j);
		}

		// Responem en funció de si la primera posició és guanyadora
		cout << (es_posicio_guanyadora(0) ? "Max" : "Izan") << endl;
	}
}