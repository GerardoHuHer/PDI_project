"""
    Crea una rutina en la que realices una segmetación de una foto seleccionada.
"""
from PIL import Image


def segmentacion(path: str) -> str:
    """
        Función para generar la segmentación por canales del rgb.
    """
    try:
        img = Image.open(path)
        img.show()
        img2 = img.copy()
        mbits = list(img2.getdata())
        segmento = list(map((
            lambda pixel: pixel if (pixel[2] > 63 and pixel[2] < 122)
            else tuple(255 for canal in pixel)), mbits))
        img2.putdata(segmento)
        img2.show()
        return "Se ha modificado la imagen con éxito."
    except FileNotFoundError:
        return "La imagen no existe."
    except:
        return "Ha habido un problema al modificar la imagen."


segmentacion("/home/gd_15/Descargas/colores.jpg")
