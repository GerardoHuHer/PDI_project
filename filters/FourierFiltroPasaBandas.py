# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 13:21:23 2024

@author: Eduardo
"""



import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
imagen = cv2.imread('C:/Users/Eduardo/OneDrive - Grupo UniCCo/Clases UP (Licenciatura)/imagenes/flowers.jpg', cv2.IMREAD_GRAYSCALE)


# Dimensiones de la imagen
h, w = imagen.shape
centro_x, centro_y = h // 2, w // 2

# Definir radios para el filtro pasa-bandas o rechaza-bandas
radio_externo = 60  # Radio del círculo más grande
radio_interno = 20  # Radio del círculo más pequeño

# Calcular la Transformada de Fourier
f = np.fft.fft2(imagen)
f_shift = np.fft.fftshift(f)  # Desplazar el cero de frecuencia al centro


# Crear un filtro pasa-bandas
filtro_pasa_bandas = np.zeros((h, w))
cv2.circle(filtro_pasa_bandas, (centro_x, centro_y), radio_externo, 1, -1)
cv2.circle(filtro_pasa_bandas, (centro_x, centro_y), radio_interno, 0, -1)

# Aplicar el filtro pasa-bandas al espectro
f_shift_filtrado = f_shift * filtro_pasa_bandas

# Transformada inversa para obtener la imagen filtrada
f_inv_shift = np.fft.ifftshift(f_shift_filtrado)
imagen_pasa_bandas = np.abs(np.fft.ifft2(f_inv_shift))

# Mostrar la imagen filtrada
plt.imshow(imagen_pasa_bandas, cmap='gray')
plt.title('Imagen con Filtro Pasa-Bandas')
plt.show()


