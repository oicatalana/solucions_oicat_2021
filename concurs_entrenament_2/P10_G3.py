from PIL import Image, ImageDraw

# Llegim les variables
c1 = input()
c2 = input()
x1 = int(input())
x2 = int(input())
y1 = int(input())
y2 = int(input())
e = int(input())
k = int(input())

# Dimensions de la imatge
X = x2 - x1 + 1
Y = y2 - y1 + 1

# Creem la imatge
img = Image.new('RGB', (X, Y))
dib = ImageDraw.Draw(img)

# Funció per decidir si el punt c = c_real + c_imag · i és al conjunt
# Retornem el color corresponent (c1 si hi pertany, c2 si no)
def color_mandelbrot(c_real, c_imag):
    # Comencem amb z = z_real + z_imag · i = 0
    z_real, z_imag = 0, 0
    
    for i in range(k):
        # Actualitzem: z = f_c(z)
        z_real, z_imag = z_real**2 - z_imag**2 + c_real, 2*z_real*z_imag + c_imag

        # Si |z|² = z_real² + z_imag² > 4, el punt no és de Mandelbrot
        if z_real**2 + z_imag**2 > 4:
            return c2

    # Si hem arribat aquí, considerem que el punt és de Mandelbrot
    return c1

# Pintem cada punt de la imatge amb el color que toca
for i in range(X):
    for j in range(Y):
        dib.point((i, j), color_mandelbrot((x1 + i)/e, (y1 + j)/e)) 

# Guardem la imatge
img.save('output.png')
