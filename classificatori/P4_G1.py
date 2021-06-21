from PIL import Image, ImageDraw

# Llegim la entrada
n = int(input())
k = int(input())

# Creem la imatge.
img = Image.new('RGB', [n, n], 'Beige')
dib = ImageDraw.Draw(img)

# Paràmetres del rectangle
min_x = n
max_x = 0
min_y = n
max_y = 0

punts = []  # Llista de punts

# Llegim cada punt, el guardem, i actualitzem els paràmtres del rectangle
for i in range(k):
    x = int(input())
    y = int(input())
    punts.append((x, y))
    min_x = min(x, min_x)
    max_x = max(x, max_x)
    min_y = min(y, min_y)
    max_y = max(y, max_y)

# Dibuixem el rectangle
dib.polygon([(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)], 'Red')

# Dibuixem cada punt
for punt in punts:
    dib.point(punt, 'Black')

# Guardem la imatge
img.save('output.png')
