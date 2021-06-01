#include <iostream>
using namespace std;

typedef long long int LL;

int main() {
    LL n;
    while (cin >> n) {
        // La solució estarà a l'interval [l, r)
        LL l = 0;
        LL r = 1414214;
         
        // Mentre [l, r) tingui més d'un element:
        while (r - l > 1) {
            // Agafem el punt mig m de l'interval
            LL m = (r + l)/2;

            // Si 1 + ... + m <= n, la solució estarà a [m, r),
            // i si no, estarà a [l, m)
            if (m*(m + 1)/2 <= n)
                l = m;
            else
                r = m;
        }

        // Al final ens quedem amb l'interval [l, l + 1), que només
        // conté l'enter l: la nostra solució
        cout << l << endl;
    }
}

