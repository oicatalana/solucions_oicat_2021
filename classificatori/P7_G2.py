from PIL import Image, ImageDraw

# Llegim la entrada
n = int(input())
s = int(input())

# Funció per calcular 1 + 2 + ... + k
def S(k):
    return k*(k + 1)//2

# Creem la imatge. Posem 'Blue' de color de fons per evitar pintar els rectangles dels extrems
img = Image.new('RGB', [S(n)*s, S(n)*s], 'Blue')
dib = ImageDraw.Draw(img)

# Dibuixa un quadrat de costat s*i amb cantonada superior esquerra a (s*x, s*y)
def dibuixa_quadrat(x, y, i, col):
    dib.polygon([(s*x, s*y), (s*(x + i) - 1, s*y), (s*(x + i) - 1, s*(y + i) - 1), (s*x, s*(y + i) - 1)], col)

# Donada una k, diu el color del quadrat del "centre" de la franja
def color_inicial(k):
    return {0: 'Blue', 1: 'Yellow', 2: 'Lime', 3: 'Red'}[k%4]

# Donat un color, retorna l'altre color de la franja
def canvia_color(col):
    return {'Yellow': 'Red', 'Red': 'Yellow', 'Lime': 'Blue', 'Blue': 'Lime'}[col]

# Iterem per cada franja
for i in range(1, n + 1):
    # Dibuixem el "centre" de la franja, amb el color pertinent
    x = S(i - 1)
    y = S(n) - S(i)
    col = color_inicial(i)
    dibuixa_quadrat(x, y, i, col)

    # Dibuixem la resta de quadrats
    for j in range(1, (i + 1)//2):
        col = canvia_color(col)     # Canvia el color a cada pas
        dibuixa_quadrat(x, y + i*j, i, col) # Dibuixa del centre cap abaix
        dibuixa_quadrat(x - i*j, y, i, col) # Dibuixa del centre cap a l'esquerra

# Guardem la imatge
img.save('output.png')
