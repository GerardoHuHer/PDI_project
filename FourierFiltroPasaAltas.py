# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:15:06 2024

@author: Eduardo
"""


import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
imagen = cv2.imread("D:\\Procesamiento_Imagenes_UP\\TareaMascaras\\arbol.jpg",  cv2.IMREAD_GRAYSCALE)


h, w = imagen.shape
centro_x, centro_y = h // 2, w // 2
radio = 30  # Tamaño del filtro (ajustable)

# Calcular la Transformada de Fourier
f = np.fft.fft2(imagen)
f_shift = np.fft.fftshift(f)  # Desplazar el cero de frecuencia al centro


# Crear un filtro pasa-altas
filtro_pasa_altas = np.ones((imagen.shape[0], imagen.shape[1]))
cv2.circle(filtro_pasa_altas, (centro_x, centro_y), radio, 0, -1)

# Aplicar el filtro pasa-altas en el espectro
f_shift_filtrado = f_shift * filtro_pasa_altas

# Transformada inversa para obtener la imagen filtrada
f_inv_shift = np.fft.ifftshift(f_shift_filtrado)
imagen_pasa_altas = np.abs(np.fft.ifft2(f_inv_shift))

# Mostrar la imagen
plt.imshow(imagen_pasa_altas, cmap='gray')
plt.title('Imagen con Filtro Pasa-Altas')
plt.show()