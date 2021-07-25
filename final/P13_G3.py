from PIL import Image, ImageDraw

# Llegim les dimensions del mapa
d = int(input())
p = int(input())
a = int(input())
col = [input() for _ in range(a)]

# El nombre de columnes que haurà de tenir la nostra imatge
h = (a**p - a)//p

# Creem la imatge
img = Image.new("RGB", (d*h, d*p), 'Black')
dib = ImageDraw.Draw(img)

sol = []        # Llista de coloracions vàlides
v = [None]*p    # Coloració provisional

# Funció que dirà si una coloració és monocromàtica
def es_monocromatica():
    for i in range(p):
        if v[i] != v[0]:
            return False
    return True

# Funció que dirà si una la coloració v = (v_0, ..., v_{p - 1}) és lexicogràficament menor
# Per a comprovar-ho, compararà v amb totes les coloracions cíclicament equivalents
# (v_i, ..., v_{p - 1}, v_0, ..., v_{i - 1})
# Com podeu veure, podem fer això aprofitant-nos de les opcions que ofereix Python
def es_lexicograficament_menor():
    for i in range(p):
        if v[i:] + v[:i] < v:
            return False
    return True

# Backtracking per calcular totes les coloracions possibles
# Ens guardem la coloració provisional a v, i x ens indica vidres hem afegit
def backtracking(x):
    # Si el collaret té els p vidres, mirem si la coloració és valida,
    # i si ho és l'afegim a la llista de solucions
    if x == p:
        if not es_monocromatica() and es_lexicograficament_menor():
            # Compte!!! Cal crear una copia de v! Fer sol.append(v) en portarà problemes
            sol.append(v[:])         
        return
    # Si encara no les hem pintat totes, afegim un nou vidre i avancem amb el backtracking
    for i in range(a):
        v[x] = i
        backtracking(x + 1)

# Comencem un backtracking havent posat 0 vidres al collaret,
# amb el que obtindrem totes les coloracions vàlides
backtracking(0)

# Dibuixem les solucions que hem obtingut
for x in range(h):
    for y in range(p):
        dib.ellipse([(d*x, d*y), (d*(x + 1) - 1, d*(y + 1) - 1)], col[sol[x][y]])

# Guardem la imatge
img.save('output.png')