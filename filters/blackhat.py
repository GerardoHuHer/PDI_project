
import cv2
import numpy as np

path: str = "D:\\Procesamiento_Imagenes_UP\\TareaMascaras\\arbol.jpg"
# Cargar la imagen binaria
imagen = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Definir el elemento estructurante
elemento_estructurante = np.ones((17, 17), np.uint8)

# Aplicar el cierre
imagen_cierre = cv2.morphologyEx(imagen, cv2.MORPH_CLOSE, elemento_estructurante)

# Calcular la operación Black-Hat
black_hat = cv2.subtract(imagen_cierre, imagen)

# Mostrar el resultado de la operación Black-Hat
cv2.imshow('Imagen Original', imagen)
cv2.imshow('Black-Hat', black_hat)
cv2.waitKey(0)
cv2.destroyAllWindows()
