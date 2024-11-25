# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 20:15:38 2024

@author: etejada
"""

import cv2

# Cargar el clasificador Haar para detección de rostros (asegúrate de tener el archivo haarcascade_frontalface_default.xml)
cascade_rostro = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Iniciar la cámara
cap = cv2.VideoCapture(0)

while True:
    # Capturar el cuadro de la cámara
    ret, frame = cap.read()
    
    # Convertir la imagen a escala de grises (necesario para la detección de rostros)
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detectar rostros en la imagen
    rostros = cascade_rostro.detectMultiScale(gris, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    
    # Dibujar rectángulos alrededor de los rostros detectados
    for (x, y, w, h) in rostros:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Mostrar el cuadro con los rostros detectados
    cv2.imshow('Detección de Rostros en Tiempo Real', frame)
    
    # Romper el bucle si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()

