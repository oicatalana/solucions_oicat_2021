#include <iostream>
using namespace std;

typedef long long int LL;

// Diu si x pertany a range(0, n, d), assumint que d > 0
void resol(LL x, LL n, LL d) {
    cout << (x%d == 0 and 0 <= x and x < n ? "SI" : "NO") << endl;
}

int main() {
    LL x, k;
    while (cin >> x >> k) {
        if (k == 1) {
            LL n;
            cin >> n;
            // x pertany a range(n) si i només si x pertany a range(0, n, 1)
            resol(x, n, 1);
        }
        if (k == 2) {
            LL a, b;
            cin >> a >> b;
            // x pertany a range(a, b) si i només si x - a pertany a range(0, b - a, 1)
            resol(x - a, b - a, 1);
        }
        if (k == 3) {
            LL a, b, d;
            cin >> a >> b >> d;
            if (d > 0)
                // x pertany a range(a, b, d) si i només si x - a pertany a range(0, b - a, d)
                resol(x - a, b - a, d);
            else
                // x pertany a range(a, b, d) si i només si a - x pertany a range(0, a - b, -d)
                resol(a - x, a - b, -d);
        }
    }
}
