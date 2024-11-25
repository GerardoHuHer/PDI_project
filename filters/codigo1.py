'''
    Generar un negativo dada una imagen a color.
'''
import time
from PIL import Image

def negativo_grises2(im):
    tiempoIn = time.time()
    ruta = ("/home/gd_15/Descargas/" + im)
    im = Image.open(ruta)
    print(f"Este es el tipo de la imagen: {type(im)}")
    im.show()
    im15 = im.copy()
    im15 = im15.convert("L")
    width, height = im15.size

    for i in range(width):
        for j in range(height):
            pixel = im15.getpixel((i,j))
            # pixel = (255 - pixel[0], 255-pixel[1], 255-pixel[2]) # Tres canales
            im15.putpixel((i,j), 255 - pixel) # Un canal 
            im15.putpixel((i,j), pixel)

    im15.show()
    tiempoFin = time.time()
    print(f"El proceso tarde: {tiempoFin - tiempoIn}, segundos ")
            
negativo_grises2("obsidian.png")
