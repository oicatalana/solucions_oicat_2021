#include <iostream>
#include <vector>
using namespace std;

//  Definicions  //

struct Provincia {
    string nom;
    string capital;
    int habitants;
    int area;
    double pib;
};

struct Pais {
    string nom;
    string capital;
    vector<Provincia> provs;
};

typedef vector<Pais> Paisos;

int habitants(const Paisos& p, double x) {
    int total = 0;

    // Per cada país, comptem els seus habitants, i el seu
    // nombre de "províncies pobres" (amb PIB <= x)
    for (const Pais& pais : p){
        int provincies_pobres = 0;
        int habitants_pais = 0;

        // Per cada província, mirem si és "pobra",
        // i actualitzem la població del país
        for (const Provincia& prov : pais.provs){
            habitants_pais += prov.habitants;
            if (prov.pib <= x)
                ++provincies_pobres;
        }

        // Si hi ha 2 o més províncies pobres, actualitzem la solució
        if (provincies_pobres >= 2)
            total += habitants_pais;
    }

    // Retornem la solució
    return total;
}