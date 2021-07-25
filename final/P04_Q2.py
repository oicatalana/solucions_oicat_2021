from math import isqrt

suma_total = 0.
for i in range(1, 10**8):
    if i%(10**5) == 0:
        print(i, suma_total)
    if isqrt(100*i + 25)**2 == 100*i + 25:
        suma_total += 1/i
