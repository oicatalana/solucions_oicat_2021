#include <iostream>
#include <queue>
using namespace std;

int main(){
    priority_queue <int> PQ;
    char c;
    while (cin >> c){
        // Afegir un enter a la priority queue
        if (c == 'S'){
            int x;
            cin >> x;
            PQ.push(x);
        }
        
        // La resta d'operacions només son viables si la nostra
        // priority queue no està buida.
        // Si ho està, escrivim un missatge d'error, i continuem
        if (PQ.empty()) {
            cout << "error!" << endl;
            continue;
        }

        // Consultar el nombre més gran
        if (c == 'A')
            cout << PQ.top() << endl;

        // Esborrar el nombre més gran
        if (c == 'R')
            PQ.pop();

        // Incrementar el nombre més gran en x unitats
        if (c == 'I') {
            int x;
            cin >> x;               // Llegim x
            int val = x + PQ.top(); // Calculem el nou valor
            PQ.pop();               // Eliminem l'antic màxim valor
            PQ.push(x);             // Afegim el nou valor
        }

        // Decrementar el nombre més gran en x unitats
        if (c == 'D'){
            int x;
            cin >> x;               // Llegim x
            int val = x + PQ.top(); // Calculem el nou valor
            PQ.pop();               // Eliminem l'antic màxim valor
            PQ.push(x);             // Afegim el nou valor
        }
    }
}