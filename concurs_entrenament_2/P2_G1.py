from PIL import Image, ImageDraw

# Llegim variables
r = int(input())
g = int(input())
b = int(input())

# Creem imatge
img = Image.new('RGB', (900, 300), 'Black')
dib = ImageDraw.Draw(img)

# Dibuixem els rectangles
for i in range(6):
    color = ((5 - i)*r // 5, (5 - i)*g // 5, (5 - i)*b // 5)
    dib.polygon([(150*i, 0), (150*i + 149, 0), (150*i + 159, 299), (150*i, 299)], color)

# Guardem la imatge
img.save('output.png')
