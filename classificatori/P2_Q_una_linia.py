from math import sqrt

print([i for i in range(404, 10**6, 404) if int(sqrt(100*i + 25))**2 == 100*i + 25][0])
