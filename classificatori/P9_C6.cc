#include <iostream>
using namespace std;

string codificacio;
string paraula;

// Convertim el p-èssim dígit de l'string al seu valor numèric
int to_int(int p) {
    return codificacio[p] - '0';
}

// Convertim un valor numèric a la seva lletra corresponent
char to_char(int x) {
    return 'A' + x - 1;
}

// Anem escrivint caràcters des del p-èssim dígit de la codificació
void backtracking(int p) {
    // Si ja hem tractat tota la codificació, imprimim
    if (p == codificacio.size()) {
        cout << paraula << endl;
        return;
    }

    // El següent dígit no pot començar en 0, si hi comença, abortem
    if (codificacio[p] == '0')
        return;

    // Convertim un dígit en un caràcter, l'afegim a la resposta, i continuem 
    paraula.push_back(to_char(to_int(p)));
    backtracking(p + 1);
    paraula.pop_back();     // En aquest punt, desfem el canvi

    // Intentem crear un caràcter amb els dos següents dígits
    if (p + 1 != codificacio.size()) {
        int val = 10*to_int(p) + to_int(p + 1);
        if (val <= 26) {
            // Igual que abans, afegim el caràcter a la resposta, i continuem
            paraula.push_back(to_char(val));
            backtracking(p + 2);
            paraula.pop_back();     // Desfem el canvi
        }
    }
}

int main() {
    while (cin >> codificacio) {
        backtracking(0);
        cout << string(10, '-') << endl;
    }
}