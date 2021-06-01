import sys

for paraula in sys.stdin:
    print(("le " + paraula).replace("oi", "ua").replace("r", "rg").replace("nt\n", "ng\n").rstrip('\n'))
