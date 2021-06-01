from PIL import Image, ImageDraw

# Llegim les variables
f = input()
t = input()
n = int(input())
m = int(input())

# Creem la imatge (de dimensions (n, m) i fons f)
img = Image.new('RGB', (n, m), f)
dib = ImageDraw.Draw(img)

# Dibuixem el triangle
dib.polygon([(0, 0), (n//2, n//2), (n - 1, 0)], t)

# Guardem la imatge
img.save('output.png')
