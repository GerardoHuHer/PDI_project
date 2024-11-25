
import cv2
import numpy as np

path: str = "D:\\Procesamiento_Imagenes_UP\\TareaMascaras\\arbol.jpg"
imagen = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Definir el elemento estructurante
elemento_estructurante = np.ones((5, 5), np.uint8)

# Aplicar la apertura
imagen_apertura = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, elemento_estructurante)

# Calcular la operación Top-Hat
top_hat = cv2.subtract(imagen, imagen_apertura)

# Mostrar el resultado de la operación Top-Hat
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Top-Hat', top_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
