import cv2
import numpy as np
import matplotlib.pyplot as plt

path: str = "D:\\Procesamiento_Imagenes_UP\\binaria.png"
imagen = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

bordes = cv2.Canny(imagen, 100, 130)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(bordes, cmap='gray')
plt.title('Filtro de Canny')
plt.axis('off')

plt.show()