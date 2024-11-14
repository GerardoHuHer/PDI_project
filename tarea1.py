'''
    Tarea 1: Generar un código que dada una imagen a color nos devuelva su negativo
'''
from PIL import Image

def imagenNegativo(path: str) -> str:
    '''
        Función que recibe el path de la imagen y devuelve su negativo
    '''
    try:        
        img = Image.open(path)
        img.show()
        img2 = img.copy()
        pixels = list(img2.getdata())
        negativo = list(map(lambda pixel: (255 - pixel[0], 255 - pixel[1], 255 - pixel[2]), pixels))
        img2.putdata(negativo)
        img2.show()
        return "Se ha creado el negativo de la foto."
    except:
        return "Fallo al realizar las modificaciones a la foto."

    

def blancoNegro(path: str) -> str:
    '''
        Función para pasar a escala de grises una imagen
    '''
    try:
        img = Image.open(path)
        img.show()
        img2 = img.copy()
        img2 = img2.convert("L")
        pixels = list(img2.getdata())
        grises = list(map(lambda pixel: (255 - pixel), pixels))
        img2.putdata(grises)
        img2.show()
        return "La foto se ha modificado correctamente"
    except:
        return "Fallo al modificar la foto."

# print(imagenNegativo("/home/gd_15/Descargas/obsidian.png"))
# print(blancoNegro("/home/gd_15/Descargas/obsidian.png"))
print(imagenNegativo("/home/gd_15/Descargas/colores.jpg"))
print(blancoNegro("/home/gd_15/Descargas/colores.jpg"))


