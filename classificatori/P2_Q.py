from math import sqrt

for i in range(404, 10**9, 404):
    if int(sqrt(100*i + 25))**2 == 100*i + 25:
        print(i)
        break
