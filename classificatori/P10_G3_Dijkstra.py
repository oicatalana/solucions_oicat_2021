from PIL import Image, ImageDraw
from queue import PriorityQueue

# Llegim les dimensions del mapa
n = int(input())
m = int(input())

# Creem la imatge
img = Image.new('RGB', (25*m, 25*n))
dib = ImageDraw.Draw(img)

# Llegim el mapa
mapa = [input() for i in range(n)]

# Llegim els colors
c = int(input())
colors = [input() for i in range(c)]

# Funció per dibuixar la casella amb coordenades (x, y)
def dibuixa_casella(y, x, col):
    dib.polygon([(25*x, 25*y), (25*x + 24, 25*y), (25*x + 24, 25*y + 24), (25*x, 25*y + 24)], col)

# Funció per dibuixar un forat a la casella amb coordenades (x, y)
def dibuixa_forat(y, x, col):
    dib.ellipse([25*x + 5, 25*y + 5, 25*x + 19, 25*y + 19], col)

# Dibuixem el mapa i ens guardem la casella d'entrada
entrada = None
for i in range(n):
    for j in range(m):
        dibuixa_casella(i, j, 'Brown' if mapa[i][j] == 'X' else 'White')
        if mapa[i][j] == 'O':
            dibuixa_forat(i, j, 'Black')
        if mapa[i][j] == 'E':
            entrada = (i, j)

# Per a cada casella, ens guardem el cost mínim amb el que hi podem arribar,
# i el pare (una casella des d'on venir per aconseguir aquest cost mínim)
cost = [[(0, 0) if (i, j) == entrada else (100, 0) for j in range(m)] for i in range(n)]
pare = [[None for j in range(m)] for i in range(n)]

# Tractem el pare del vèrtex inicial com un cas especial
pare[entrada[0]][entrada[1]] = (-1, -1)

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]      # Llista de desplaçaments possibles
sortida = None                                  # Guardarem aquí la casella de sortida
min_blocs = None                                # I aquí el mínim nombre de blocs usats a la solució òptima

# La nostra priority queue guardarà estats (k, d, x, y),
# que indicarà que podem arribar a la casella (x, y) usant k blocs i amb distància d.
# Aquesta priority queue guarda els seus estats de menor a major,
# i per tant només podrem accedir, d'entre els que tinguin menor k,
# al que tingui menor distància d.
pq = PriorityQueue()

# Afegim l'estat inicial a pq (començar a l'entrada amb 0 blocs i distància d)
pq.put((0, 0, entrada[0], entrada[1]))

## Dijkstra:
while not pq.empty():
    # Obtenim l'element mínim de pq, i l'esborrem de pq
    k, d, x, y = pq.get()

    # Si la posició ja ha estat visitada prèviament, continuem
    if cost[x][y] < (k, d):
        continue

    # Si la nostra posició és una sortida, haurem trobat el camí òptim i parem
    if mapa[x][y] == 'S':
        sortida = (x, y)
        min_blocs = k + 1
        break

    # Mirem el proper nombre de blocs usats K un cop hem passat per la casella
    K = k + 1 if mapa[x][y] == 'O' else k

    # Per cada casella adjacent, si no és un obstacle i millorem el cost mínim,
    # actualitzem aquest cost, assignem el pare, i afegim el nou estat a pq 
    for dx, dy in delta:
        X, Y = x + dx, y + dy
        if (K, d + 1) < cost[X][Y] and mapa[X][Y] != 'X':
            cost[X][Y] = (K, d + 1)
            pare[X][Y] = (x, y)
            pq.put((K, d + 1, X, Y))

i, j = sortida[0], sortida[1]       # Posició d'una casella del camí òptim (començant pel final)
ind = min_blocs                     # Nombre de blocs usats en aquest camí

# Anem desfent el camí des de la sortida, amb l'ajut del que hem guardat a pare
# i sobrescrivint les caselles i els forats en el dibuix amb els colors pertinents
while (i, j) != (-1, -1):
    dibuixa_casella(i, j, "Darkseagreen")
    if mapa[i][j] in ['O', 'S']:
        dibuixa_forat(i, j, colors[ind - 1])
        ind -= 1
    i, j = pare[i][j]

# Guardem la imatge
img.save('output.png')