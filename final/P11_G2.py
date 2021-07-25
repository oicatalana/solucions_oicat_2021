from PIL import Image, ImageDraw

# Llegim les variables, els colors, i les direccions
n = int(input())
k = int(input())
m = int(input())

cols = [None]*m
dirs = [None]*m
for i in range(m):
    cols[i] = input()
    dirs[i] = input()

# Creem la imatge
img = Image.new('RGB', [n, n], cols[0])
dib = ImageDraw.Draw(img)

# Creem el mapa
mapa = [[0]*n for _ in range(n)]

# Llista de possibles direccions
delta = [(1, 0), (0, -1), (-1, 0), (0, 1)]

# Posició i direcció inicial de la formiga 
px, py = n//2, n//2
dir = 1                 # Comença mirant cap al nord

# A cadascun dels k passos
for i in range(k):
    # Mirem l'índex del nou color
    ind = (mapa[py][px] + 1)%m

    # Pintem el punt del nou color, i l'actualitzem al mapa
    dib.point((px, py), cols[ind])
    mapa[py][px] = ind

    # Actualitzem la posició i la direcció de la formiga
    dir = (dir + 1 if dirs[ind] == 'E' else dir - 1)%4
    dx, dy = delta[dir]
    px, py = px + dx, py + dy

# Guardem la imatge
img.save('output.png')
