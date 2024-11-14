# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 17:43:54 2024

@author: Eduardo
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Cargar la imagen en escala de grises
imagen = cv2.imread("C:/Users/Eduardo/OneDrive - Grupo UniCCo/Clases UP (Licenciatura)/imagenes/onerice.png", cv2.IMREAD_GRAYSCALE)

# 1. Negativo de la imagen
negativo = 255 - imagen

# 2. Transformación Logarítmica
c = 255 / np.log(1 + np.max(imagen))
logaritmica = c * np.log(1 + imagen)

# 3. Transformación Gamma
gamma = 2.0  # Ejemplo con gamma = 2.0
gamma_correccion = np.array(255 * (imagen / 255) ** gamma, dtype='uint8')

# Mostrar las imágenes
imagenes = [imagen, negativo, logaritmica, gamma_correccion]
titulos = ['Original', 'Negativo', 'Logarítmica', 'Gamma']

for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(imagenes[i], cmap='gray')
    plt.title(titulos[i])
    plt.xticks([]), plt.yticks([])

plt.show()
