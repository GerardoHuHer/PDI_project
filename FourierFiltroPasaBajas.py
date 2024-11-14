#'C:/Users/Eduardo/OneDrive - Grupo UniCCo/Clases UP (Licenciatura)/imagenes/onerice.png' -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:10:12 2024

@author: Eduardo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
imagen = cv2.imread("D:\\Procesamiento_Imagenes_UP\\TareaMascaras\\arbol.jpg", cv2.IMREAD_GRAYSCALE)

# Crear un filtro de paso bajo (low-pass) en el dominio frecuencial
h, w = imagen.shape
centro_x, centro_y = h // 2, w // 2
radio = 30  # Tamaño del filtro (ajustable)

# Calcular la Transformada de Fourier
f = np.fft.fft2(imagen)
f_shift = np.fft.fftshift(f)  # Desplazar el cero de frecuencia al centro

# Crear una máscara de paso bajo
filtro_paso_bajo = np.zeros((h, w), dtype=np.uint8)
cv2.circle(filtro_paso_bajo, (centro_x, centro_y), radio, 1, -1)

# Aplicar el filtro
f_shift_filtrado = f_shift * filtro_paso_bajo

# Transformada inversa para obtener la imagen filtrada
f_inv_shift = np.fft.ifftshift(f_shift_filtrado)
imagen_filtrada = np.fft.ifft2(f_inv_shift)
imagen_filtrada = np.abs(imagen_filtrada)

# Mostrar la imagen filtrada
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(imagen_filtrada, cmap='gray')
plt.title('Imagen Filtrada (Low-pass)')
plt.show()
