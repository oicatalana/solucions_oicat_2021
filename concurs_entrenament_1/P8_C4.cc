#include <vector>
using namespace std;

int posicio(double x, const vector<double> &v, int esq, int dre) {
    // Si esq > dre, retornem -1.
    // Observeu que podem arribar aquí tant si els valors que ens
    // dona el jutge de esq i dre compleixen esq > dre,
    // com si x no pertany a l'interval [esq, dre] donat
    if (esq > dre)
        return -1;

    // Calculem el "punt mig" m 
    int m = (esq + dre)/2;

    // Si hem trobat x a v[m], retornem la posició m
    if (v[m] == x)
        return m;

    // Si v[m] és més gran que x, només podrem trobar x a l'interval [esq, m - 1]
    else if (v[m] > x)
        return posicio(x, v, esq, m - 1);

    // I si és més petit, només el podrem trobar a [m + 1, dre]
    else
        return posicio (x, v, m + 1, dre);
}