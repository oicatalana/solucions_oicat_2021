from PIL import Image, ImageDraw
from math import sqrt

# Llegim la entrada
n = int(input())
x = int(input())
y = int(input())
vp = float(input())
vg = float(input())

# Funció per calcular el temps total que triga el nen si surt pel punt (5n, r)
def t(r):
    return sqrt((5*n)**2 + r**2)/vp + sqrt((x - 5*n)**2 + (y - r)**2)/vg

# Calculem el temps mínim i la k que el minimitza
temps_minim = 10.**10
millor_k = None

for k in range(1, n):
    temps = t(10*k)
    if temps < temps_minim:
        temps_minim = temps
        millor_k = k

# Creem la imatge. Posem LawnGreen de fons per evitar fer dos rectangles
img = Image.new('RGB', (10*n, 10*n), 'LawnGreen')
dib = ImageDraw.Draw(img)

# Dibuixem la meitat corresponent a la piscina
dib.polygon([(0, 0), (5*n - 1, 0), (5*n - 1, 10*n - 1), (0, 10*n - 1)], 'Aqua')

# Dibuixem els segments, tal i com indica l'enunciat
dib.line([(0, 0), (5*n, 10*millor_k)], 'Black')
dib.line([(5*n, 10*millor_k), (x, y)], 'Black')

# Guardem la imatge
img.save('output.png')
