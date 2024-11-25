import cv2
import numpy as np
import matplotlib.pyplot as plt

imagen = cv2.imread('.\\arbol.jpg', cv2.IMREAD_GRAYSCALE)

suavizado = np.ones((3, 3), np.float32) / 9
print(suavizado)
imagen_suavizada = cv2.filter2D(imagen, -1, suavizado)

bordes_sobel = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
imagen_bordes = cv2.filter2D(imagen, -1, bordes_sobel)

imagenes = [imagen, imagen_suavizada, imagen_bordes]
titulos = ['Original', 'Suavizado', 'Bordes (Sobel)']

for i in range(3):
    plt.subplot(1, 3, i+1)
    plt.imshow(imagenes[i], cmap='gray')
    plt.title(titulos[i])
    plt.xticks([]), plt.yticks([])

plt.show()
