'''

'''
from PIL import Image
import matplotlib.pyplot as plt


def ajustar_brillo(img, factor):
    img_modificada = img.copy()
    ancho, alto = img.size
    for x in range(ancho):
        for y in range(alto):
            r, g, b = img.getpixel((x, y))
            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)

            r = min(255, max(0, r))
            g = min(255, max(0, g))
            b = min(255, max(0, b))

            img_modificada.putpixel((x, y), (r, g, b))
    return img_modificada


img = Image.open("/home/gd_15/Descargas/colores.jpg")

plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.title("Imagen Original")
plt.imshow(img)

aumentado = ajustar_brillo(img, 1.5)
plt.subplot(1, 3, 2)
plt.title("Brillo aumentado")
plt.imshow(aumentado)

img_brillo_disminuido = ajustar_brillo(img, 0.5)
plt.subplot(1, 3, 3)
plt.title("Brillo disminuido")
plt.imshow(img_brillo_disminuido)
