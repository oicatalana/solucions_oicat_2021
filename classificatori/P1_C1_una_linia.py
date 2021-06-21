import sys

for line in sys.stdin:
	print("no" if len(set(map(int, line.rstrip('\n').split()[1:]))) == 1 else "si")
