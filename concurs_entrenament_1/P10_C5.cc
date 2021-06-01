#include <iostream>
#include <vector>
using namespace std;

vector<vector<bool>> visitable;   // Per a cada casella, diu si la podem visitar
vector<vector<bool>> es_bolet;    // Per a cada casella, diu si hi ha un bolet

// Direccions (est, nord, oest, sud) en les que en Pac-man es pot moure
int dx[] = {1, 0, -1, 0};
int dy[] = {0, -1, 0, 1};

// Retornem true si podem accedir a una posició amb bolet 
bool dfs(int x, int y) {
    // Si la posició no és visitable, abortem la cerca
    if (!visitable[x][y])
        return false;

    // Si la posició té un bolet, retornem true
    if (es_bolet[x][y])
        return true;

    // Marquem la posició com a no visitable per no tornar-hi en el futur
    visitable[x][y] = false;

    // Explorem cada casella adjacent recursivament. Si en alguna d'aquestes
    // exploracions hem trobat un bolet, retornem true...
    for (int i = 0; i < 4; ++i)
        if (dfs(x + dx[i], y + dy[i]))
            return true;

    // ... i si no, retornem false.
    return false;
}

int main() {
    int n, m;
    while (cin >> n >> m) {
        // Per cada casella, guardem si és visitable. Per defecte, totes ho són.
        visitable = vector<vector<bool>>(n, vector<bool>(m, true));

        // Per cada casella, guardem si té un bolet. Per defecte, no cap en té.
        es_bolet = vector<vector<bool>>(n, vector<bool>(m, false));

        // Posició inicial del Pac-man
        int pacman_x, pacman_y;

        // Llegim el mapa
        for (int x = 0; x < n; ++x) {
            string fila;
            cin >> fila;
            for (int y = 0; y < m; ++y) {
                // Si la casella és un obstacle, no és visitable
                if (fila[y] == 'X')
                    visitable[x][y] = false;

                // Si hi té un fantasma, les caselles del voltant tampoc
                else if (fila[y] == 'F')
                    for (int i : {-1, 0, 1})
                        for (int j : {-1, 0, 1})
                            visitable[x + i][y + j] = false;
                
                // Guardem la posició inicial del Pac-man
                else if (fila[y] == 'P') {
                    pacman_x = x;
                    pacman_y = y;
                }

                // Guardem si la casella té un bolet
                else if (fila[y] == 'B')
                    es_bolet[x][y] = true;
            }
        }

        // Responem en funció de si podem arribar a un bolet
        cout << (dfs(pacman_x, pacman_y) ? "si" : "no") << endl;
    }
}