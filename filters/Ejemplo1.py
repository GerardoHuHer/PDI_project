import time
from PIL import Image

tiempoIN = time.time()
ruta = "/home/gd_15/Descargas/colores.jpg"
img = Image.open(ruta)
img2 = img.copy()

w, h = img2.size
img2.show()

Y = Image.new("RGB", (w, h), color=(255, 255, 255))
Y.show()

for i in range(w):
    for j in range(h):
        pixel = img2.getpixel((i, j))
        if pixel[0] > 200 and pixel[1] < 150:
            Y.putpixel((i, j), pixel)

Y.show()
tiempoFin = time.time()
print(f"El proceso tardó, {tiempoFin-tiempoIN},  segundos")
