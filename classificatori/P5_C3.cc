#include <iostream>
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        // Anem llegint les monedes i calculem el canvi total
        int total = 0;
        for (int i = 0; i < n; ++i) {
            int moneda;
            cin >> moneda;
            total += moneda;
        }

        // Comptem el nombre de monedes del canvi mínim
        // Per fer-ho, donem tantes monedes com puguem del valor més gran
        // després tantes com puguem del segon valor més gran, etc. 
        int minim = 0;
        for (int valor : {200, 100, 50, 20, 10, 5, 2, 1}) {
            minim += total/valor;
            total %= valor;
        }

        // Depenent de si el canvi donat és "quasi-mínim", responem
        cout << (n <= minim + 1 ? "si" : "no") << endl;
    }
}