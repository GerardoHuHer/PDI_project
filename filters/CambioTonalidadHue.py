

import cv2
import numpy as np

# Cargar la imagen en color
path = "D:\\Procesamiento_Imagenes_UP\\arbol.jpg"
imagen = cv2.imread(path)

# Convertir la imagen de BGR a HSV
imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# Crear una función de trackbar para cambiar la tonalidad
def cambiar_tonalidad(x):
    # Ajustar el valor de la tonalidad
    nueva_hsv = imagen_hsv.copy()
    nueva_hsv[:, :, 0] = (nueva_hsv[:, :, 0] + x) % 180  # La tonalidad tiene un rango de 0 a 179
    nueva_imagen = cv2.cvtColor(nueva_hsv, cv2.COLOR_HSV2BGR)
    
    # Mostrar la nueva imagen
    cv2.imshow('Cambio Dinámico de Tonalidad', nueva_imagen)

# Crear una ventana y un trackbar
cv2.namedWindow('Cambio Dinámico de Tonalidad')
cv2.createTrackbar('Tonalidad', 'Cambio Dinámico de Tonalidad', 0, 179, cambiar_tonalidad)

# Mostrar la imagen original
cv2.imshow('Cambio Dinámico de Tonalidad', imagen)

# Mantener la ventana abierta hasta que se presione la tecla 'q'
while True:
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
