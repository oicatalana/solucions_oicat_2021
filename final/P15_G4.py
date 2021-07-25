from PIL import Image, ImageDraw

# Llegim la dimensió de la matriu
n = int(input())
m = 2**n

# Creem la matriu
img = Image.new('RGB', (m, m))
dib = ImageDraw.Draw(img)

# Llegim el nombre d'iteracions
k = int(input())

# Llegim la matriu de colors
matriu = [None]*m
for i in range(m):
    matriu[i] = [c for c in input()]

# Retorna una còpia del subquadrat de dimensions l x l amb costat superior esquerre a (x, y)
def copia(x, y, l):
    subq = [None]*l
    for i in range(l):
        subq[i] = [matriu[y + i][x + j] for j in range(l)]
    return subq

# Assigna els valors del subquadrat subq (de dimensions l x l)
# al subquadrat de dimensions l x l de la matriu amb costat superior esquerre a (x, y)
def assigna(x, y, subq):
    l = len(subq)
    for i in range(l):
        for j in range(l):
            matriu[y + i][x + j] = subq[i][j]

# Aplica l'algorisme a un quadrat amb costat superior esquerre a (x, y),
# tenint en compte que portem it iteracions
def blitspin(x, y, it):
    # En aquesta iteració, cada subquadrat tindrà dimensions r x r
    r = 2**(n - it)

    # Copiem cadascun dels 4 subquadrats
    sub_ul = copia(x, y, r)
    sub_ur = copia(x + r, y, r)
    sub_br = copia(x + r, y + r, r)
    sub_bl = copia(x, y + r, r)

    # Posem els 4 subquadrats al seu nou lloc
    assigna(x, y, sub_bl)
    assigna(x + r, y, sub_ul)
    assigna(x + r, y + r, sub_ur)
    assigna(x, y + r, sub_br)

    # Si no hem acabat, apliquem l'algorisme a cada subquadrat recursivament
    if it < k:
        blitspin(x, y, it + 1)
        blitspin(x + r, y, it + 1)
        blitspin(x + r, y + r, it + 1)
        blitspin(x, y + r, it + 1)

# Solucionem recursivament el problema
if k > 0:
    blitspin(0, 0, 1)

# La llista de colors
llista_colors = ['Black', 'Cyan', 'Green', 'MediumBlue', 'Orange', 'Purple', 'Red', 'White', 'Yellow']

# colors_dict[c] retorna el color que comença amb el caràcter c 
colors_dict = { s[0] : s for s in llista_colors }

# Dibuixem cada punt de la imatge
for y in range(m):
    for x in range(m):
        dib.point((x, y), colors_dict[matriu[y][x]])

# Guardem la imatge
img.save('output.png')
