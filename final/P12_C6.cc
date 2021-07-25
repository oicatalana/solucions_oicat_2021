#include <iostream>
#include <vector>
using namespace std;

constexpr int MOD = int(1e9 + 7);

// Retorna true si el dígit prové d'una lletra entre 'A' i 'I',
// és a dir, si el dígit està entre 1 i 9
bool es_valid_1_digit(char a) {
    return a != '0';
}

// Retorna true si els dos dígits provenen d'una lletra entre 'J' i 'Z',
// és a dir, si el valor que formen està entre 10 i 26
bool es_valid_2_digits(char a, char b) {
    int x = 10*(a - '0') + (b - '0');
    return x >= 10 and x <= 26;
}

int main() {
    string s;
    while (cin >> s) {
        int n = s.size();

        // dp[i]: Paraules originals agafant els primers i dígits
        vector<int> dp(n + 1, 0);
        dp[0] = dp[1] = 1;

        // Anem actualitzant el vector dp
        for (int i = 2; i <= n; ++i) {
            if (es_valid_1_digit(s[i - 1]))
                dp[i] += dp[i - 1];
            if (es_valid_2_digits(s[i - 2], s[i - 1]))
                dp[i] += dp[i - 2];
            dp[i] %= MOD;
        }

        // Escrivim la resposta
        cout << dp[n] << endl;
    }
}