#include <iostream>
using namespace std;

int main() {
    int n;
    while (cin >> n) {
        bool tots_iguals = true;
        int primer_valor;
        cin >> primer_valor;
        for (int i = 1; i < n; ++i) {
            int nou_valor;
            cin >> nou_valor;
            if (nou_valor != primer_valor)
                tots_iguals = false;
        }
        cout << (tots_iguals ? "no" : "si") << endl;
    }
}
