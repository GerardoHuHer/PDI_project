import cv2
import numpy as np

path: str = "D:\\Procesamiento_Imagenes_UP\\arbol.jpg"

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

el = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, el)

perimetro = img - erosion

cv2.imshow('Imagen Original', img)
cv2.imshow('Perimetro', perimetro)
cv2.waitKey(0)
cv2.destroyAllWindows()
