# El mateix que a P05_C2_solucio_troll.py, però més comprimit
import sys

for line in sys.stdin:
    v = list(map(int, line.rstrip('\n').split()))
    print("SI" if v[0] in range(*v[2:]) else "NO")