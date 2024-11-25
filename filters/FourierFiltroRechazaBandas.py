# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:27:27 2024

@author: Eduardo
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
path = "D:\\Procesamiento_Imagenes_UP\\TareaMascaras\\arbol.jpg"
imagen = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Aplicar la Transformada de Fourier
f_transform = np.fft.fft2(imagen)
f_shift = np.fft.fftshift(f_transform)  # Desplazar el espectro para centrarlo

# Dimensiones de la imagen
h, w = imagen.shape
centro_x, centro_y = h // 2, w // 2

# Definir radios para el filtro rechaza-banda
radio_externo = 60  # Radio del círculo externo
radio_interno = 20  # Radio del círculo interno

# Crear un filtro rechaza-banda
filtro_rechaza_banda = np.ones((h, w))
cv2.circle(filtro_rechaza_banda, (centro_x, centro_y), radio_externo, 0, -1)  # Borrar las frecuencias dentro del círculo externo
cv2.circle(filtro_rechaza_banda, (centro_x, centro_y), radio_interno, 1, -1)  # Mantener las frecuencias dentro del círculo interno

# Aplicar el filtro rechaza-banda en el espectro
f_shift_filtrado = f_shift * filtro_rechaza_banda

# Transformada inversa para obtener la imagen filtrada
f_inv_shift = np.fft.ifftshift(f_shift_filtrado)
imagen_filtrada = np.abs(np.fft.ifft2(f_inv_shift))

# Mostrar la imagen original y la imagen filtrada
plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')

plt.subplot(1, 2, 2)
plt.imshow(imagen_filtrada, cmap='gray')
plt.title('Imagen con Filtro Rechaza-Banda')
plt.show()
