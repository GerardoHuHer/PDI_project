import cv2
import numpy as np
import matplotlib.pyplot as plt


# path: str = "/home/gd_15/Escritorio/Procesamiento_Imagenes_UP/arbol.jpg"
path: str = "D:\\Procesamiento_Imagenes_UP\\arbol.jpg"

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

n: int = int(input("Ingrese el tamaño de su máscara: "))

# Máscara de n x n
el = np.ones((n,n), np.uint8)

erosion = cv2.erode(img, el, iterations=1)
dilatacion = cv2.dilate(img, el, iterations=1)

limpieza_ruido = cv2.dilate(cv2.erode(img, el,iterations=1 ), el, iterations=1)

contornos = cv2.erode(cv2.dilate(img, el,iterations=1 ), el, iterations=1)

plt.subplot(1, 5, 1)
plt.title("Original")
plt.imshow(img,cmap="gray")

plt.subplot(1, 5, 2)
plt.title("Erosión")
plt.imshow(erosion,cmap="gray")

plt.subplot(1, 5, 3)
plt.title("Dilatación")
plt.imshow(dilatacion,cmap="gray")

plt.subplot(1, 5, 4)
plt.title("Limpieza")
plt.imshow(limpieza_ruido,cmap="gray")

plt.subplot(1, 5, 5)
plt.title("Contornos")
plt.imshow(contornos,cmap="gray")

plt.show()