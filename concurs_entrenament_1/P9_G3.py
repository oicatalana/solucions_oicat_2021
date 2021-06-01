from PIL import Image, ImageDraw

n = int(input())    # Llegim les dimensions del tauler
m = (n - 1) // 2    # Índex de la fila i columna central

# Creem la imatge
img = Image.new('RGB', (90*n, 90*n))
dib = ImageDraw.Draw(img)

# f(x, y) retornarà una llista de nombres.
# 0, 1, 2 i 3 indiquen, respectivament, que cal posar un quadrat petit
# a la cantonada superior esquerra, superior dreta, inferior esquerra
# i inferior dreta del quadrat (x, y)
def f(x, y):
    if (x, y) == (m, m):
        return []
    if abs(x - m) + abs(y - m) > m:
        return []
    if x == m and y > m:
        return [0, 1]
    if x == m and y < m:
        return [2, 3]
    if y == m and x > m:
        return [0, 2]
    if y == m and x < m:
        return [1, 3]
    if min(x, y) > m or max(x, y) < m:
        return [1, 2]
    if x < m < y or x > m > y:
        return [0, 3]

# Dibuixa un quadrat amb cantonada superior esquerra a (x, y), costat l i color col 
def quadrat(x1, y1, l, col):
	dib.polygon([(x1, y1), (x1 + l - 1, y1), (x1 + l - 1, y1 + l - 1), (x1, y1 + l - 1)], col)

for i in range(n):
    for j in range(n):
        # Dibuixem el quadrat gran
        quadrat(90*i, 90*j, 90, 'Black' if (i + j) % 2 == 0 else 'White')

        # Escollim quins dels quadradets cal dibuixar...
        llista_quadrats = f(i, j)

        #... i a continuació els dibuixem amb el color pertinent
        color = 'White' if (i + j) % 2 == 0 else 'Black'
        if 0 in llista_quadrats:
            quadrat(90*i + 5, 90*j + 5, 20, color)
        if 1 in llista_quadrats:
            quadrat(90*i + 65, 90*j + 5, 20, color)
        if 2 in llista_quadrats:
            quadrat(90*i + 5, 90*j + 65, 20, color)
        if 3 in llista_quadrats:
            quadrat(90*i + 65, 90*j + 65, 20, color)

# Guardem la imatge
img.save('output.png')
