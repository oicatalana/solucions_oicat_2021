from PIL import Image, ImageDraw

# Llegim les dimensions del mapa
n = int(input())
m = int(input())

# Creem la imatge
img = Image.new("RGB", (25*m, 25*n))
dib = ImageDraw.Draw(img)

# Llegim el mapa
mapa = [input() for y in range(n)]

# Llegim els colors
c = int(input())
colors = [input() for y in range(c)]

# Funció per dibuixar la casella amb coordenades (x, y)
def dibuixa_casella(y, x, col):
    dib.polygon([(25*x, 25*y), (25*x + 24, 25*y), (25*x + 24, 25*y + 24), (25*x, 25*y + 24)], col)

# Funció per dibuixar un forat a la casella amb coordenades (x, y)
def dibuixa_forat(y, x, col):
    dib.ellipse([25*x + 5, 25*y + 5, 25*x + 19, 25*y + 19], col)

# Dibuixem el mapa i ens guardem la casella d'entrada
entrada = None
for y in range(n):
    for x in range(m):
        dibuixa_casella(y, x, "Brown" if mapa[y][x] == 'X' else 'White')
        if mapa[y][x] == 'O':
            dibuixa_forat(y, x, 'Black')
        if mapa[y][x] == 'E':
            entrada = (y, x)

# Volem tenir en compte estats (y, x, k), que ens donaran informació
# sobre com arribar a la casella (x, y) usant k blocs.
# Per a cadascun d'aquests estats, volem guardar el pare,
# que serà l'estat des d'on vindrem per aconseguir aquesta distància mínima
pare = [[[None for k in range(c + 1)] for x in range(m)] for y in range(n)]

# Tractem el pare del vèrtex inicial com un cas especial
pare[entrada[0]][entrada[1]][0] = (-1, -1, -1)

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]      # Llista de desplaçaments possibles
sortida = None                                  # Coordenades de la sortida
min_blocs = c       # Aquí guardem el mínim nombre de blocs que podem usar fins arribar a la sortida

# Trobarem la distància mínima amb un BFS, la cua la implementarem com un array.
# Només afegirem elements al final d'aquest array, i la "part frontal" de la cua
# vindrà definida per un índex que només es mourà cap a la dreta de 1 en 1.
# Els elements de la cua seran tuples (d, y, x, k), que ens indicarà que podem
# arribar al estat (y, x, k) amb distància d.
cua = [(0, entrada[0], entrada[1], 0)]
index_cua = 0

## BFS:
while index_cua < len(cua):     # Mentre que ens quedi algun element a la cua...
    # Agafem el proper estat, i movem l'índex
    d, y, x, k = cua[index_cua]
    index_cua += 1

    # Si estem a la casella de sortida, actualitzem el mínim nombre de blocs
    if mapa[y][x] == 'S':
        sortida = (y, x)
        min_blocs = min(min_blocs, k)
        continue

    # Intentem arribar a totes les caselles veïnes
    for dy, dx in delta:
        Y, X = y + dy, x + dx                       # Casella adjacent
        if mapa[Y][X] == 'X':                       # Ignorem si és un mur
            continue

        # Si la propera casella és un forat o la sortida, comptem un bloc més
        K = k + 1 if mapa[Y][X] in 'OS' else k      
        if K > c:                                   # No podem usar més de c blocs
            continue

        if pare[Y][X][K] is None:                   # Si encara no hem visitat la nova casella
            pare[Y][X][K] = (y, x, k)               # ...assignem el pare...
            cua.append((d + 1, Y, X, K))            # ...i afegim a la cua.

# Des de la sortida, anem desfent el camí, i anem dibuixant les caselles del camí òptim i els forats
y, x, ind = sortida[0], sortida[1], min_blocs

# Anem desfent el camí des de la sortida, amb l'ajut del que hem guardat a pare
# i sobrescrivint les caselles i els forats amb els colors pertinents
while (y, x) != (-1, -1):
    dibuixa_casella(y, x, "Darkseagreen")
    if mapa[y][x] in ['O', 'S']:
        dibuixa_forat(y, x, colors[ind - 1])
    y, x, ind = pare[y][x][ind]

# Guardem la imatge
img.save('output.png')
