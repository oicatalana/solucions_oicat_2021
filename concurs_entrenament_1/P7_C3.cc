#include <iostream>
using namespace std;

void dibuixa_barres(int n) {
    // Si n > 1, dibuixem dos cops el patró per n - 1
    if (n > 1) {
        dibuixa_barres(n - 1);
        dibuixa_barres(n - 1);
    }
    
    // Escrivim n asteriscos (també ho podeu fer amb un for)
    cout << string(n, '*') << endl;
}

int main(){
    int n;
    cin >> n;
    dibuixa_barres(n);
}
