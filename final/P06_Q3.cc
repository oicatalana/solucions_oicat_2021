#include <iostream>
#include <queue>
using namespace std;

typedef long long int LL;

int main() {
    // Posem 1, ..., 10^6 en una min priority queue
    priority_queue<LL, vector<LL>, greater<LL>> pq;
    for (LL i = 1; i <= 1000000; ++i)
        pq.push(i);

    // Traiem el més petit de la llista (x), i el segon més petit (y), i hi afegim 2x + y
    while (pq.size() >= 2) {
        LL x = pq.top();
        pq.pop();
        LL y = pq.top();
        pq.pop();
        pq.push(2*x + y);
    }

    // Escrivim l'únic element que queda
    cout << pq.top() << endl;
}