import sys

for line in sys.stdin:
    # Llegim les variables i les guardem a v
    v = list(map(int, line.rstrip('\n').split()))
    k = v[1]

    # Depenent del nombre d'arguments, preguntem a range si x hi pertany
    if k == 1:
        x, k, n = v
        print("SI" if x in range(n) else "NO")
    if k == 2:
        x, k, a, b = v
        print("SI" if x in range(a, b) else "NO")
    if k == 3:
        x, k, a, b, d = v
        print("SI" if x in range(a, b, d) else "NO")