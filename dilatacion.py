

import cv2
import numpy as np

# Cargar una imagen binaria
path = ".\\arbol.jpg"
imagen = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Definir el elemento estructurante
elemento_estructurante = np.ones((3, 3), np.uint8)


# Aplicar la dilatación
imagen_dilatada = cv2.dilate(imagen, elemento_estructurante, iterations=1)

# Mostrar la imagen dilatada
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Imagen Dilatada', imagen_dilatada)
cv2.waitKey(0)
cv2.destroyAllWindows()
