
import cv2
import numpy as np

path: str = "D:\\Procesamiento_Imagenes_UP\\arbol.jpg"
imagen = cv2.imread(path, cv2.IMREAD_GRAYSCALE )

elemento_estructurante = np.ones((3, 3), np.uint8)

imagen_erosionada = cv2.erode(imagen, elemento_estructurante, iterations=1)

cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Erosionada', imagen_erosionada)
cv2.waitKey(0)
cv2.destroyAllWindows()
