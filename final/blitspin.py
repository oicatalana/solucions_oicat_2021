from PIL import Image, ImageDraw
import numpy
import time

temps_inici = time.time()

## VARIABLES PER MODIFICAR:
EXP = 8         
MIDA = 2**EXP   # Mida de la imatge que volem (ha de ser una potència de 2)
ITERACIONS = 5  # Nombre d'iteracions (ha d'estar entre 0 i EXP)
INPUT_FILE = 'logo-oicat.png'   # D'on obtenim la imatge
OUTPUT_FILE = 'blitspin.png'    # On escrivim la imatge resultant

## PREPROCESSAT:

# Obrim la imatge
imatge = Image.open(INPUT_FILE)

# Adaptem la imatge a la mida que volem
imatge = imatge.resize((MIDA, MIDA))

# Convertim la imatge a una matriu:
# L'element I[i][j] defineix el píxel (i, j)
I = numpy.array(imatge)

## BLITSPIN:

# Retorna una còpia del subquadrat de dimensions l x l amb costat superior esquerre a (x, y)
def copia(x, y, l):
    return [[I[y + i][x + j].copy() for j in range(l)] for i in range(l)]

# Assigna els valors del subquadrat subq (de dimensions l x l)
# al subquadrat de dimensions l x l de la matriu amb costat superior esquerre a (x, y)
def assigna(x, y, subq):
    l = len(subq)
    for i in range(l):
        for j in range(l):
            I[y + i][x + j] = subq[i][j].copy()

# Aplica l'algorisme a un quadrat amb costat superior esquerre a (x, y),
# tenint en compte que portem it iteracions
def blitspin(x, y, it):
    # En aquesta iteració, cada subquadrat tindrà dimensions r x r
    r = MIDA//2**it

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
    if it < ITERACIONS:
        blitspin(x, y, it + 1)
        blitspin(x + r, y, it + 1)
        blitspin(x + r, y + r, it + 1)
        blitspin(x, y + r, it + 1)

# Solucionem recursivament el problema
if ITERACIONS > 0:
    blitspin(0, 0, 1)

# Convertim la matriu en imatge, i la guardem
Image.fromarray(numpy.uint8(I)).save(OUTPUT_FILE)
print(f'Imatge guardada a {OUTPUT_FILE}.')
print("El programa s'ha executat en {:.3f} segons.".
                        format(time.time() - temps_inici))
