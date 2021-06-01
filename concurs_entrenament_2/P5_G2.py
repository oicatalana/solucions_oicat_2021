from PIL import Image, ImageDraw

# Llegim variables
col = input()
n = int(input())

# Creem imatge
img = Image.new('RGB', (400, 4*n), 'Beige')
dib = ImageDraw.Draw(img)

# Degradat rectangle superior esquerra
for i in range (200):
	for j in range (2*n):
		dib.point((i, j), (0, i, 0))

# Rectangle inferior esquerra
dib.polygon([(0, 3*n), (149, 3*n), (149, 4*n - 1), (0, 4*n - 1)], col)

# Elipse
dib.ellipse([250, n, 399, 3*n - 1], 'Yellow', 'Red')

# Triangle
dib.polygon([(200, 4*n - 1), (399, 3*n), (399, 4*n - 1)], 'Orange')

# Guardem la imatge
img.save('output.png')
