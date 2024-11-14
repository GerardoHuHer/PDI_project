# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 07:20:29 2024

@author: etejada
"""

import time
from PIL import Image
#import cv2
#import numpy as np

tiempoIn = time.time()
ruta = ("C:/Users/etejada/Downloads/ImagenFiguras.png")
im = Image.open(ruta)  # Open 
#im.show()
im15 = im.copy()
#im15 = im15.convert('L')  #Convert to grayscale

width, height = im15.size
im15.show()
 
Y = Image.new('RGB', (width, height), color=(255, 255, 255))

Y.show()

for i in range(width):
        for j in range(height):
            
            pixel = im15.getpixel((i, j))
            
            if pixel[0] > 200 and pixel[1] < 150:
                Y.putpixel((i,j), pixel)
    
Y.show()

tiempoFin = time.time()
print('El proceso tardo= ', tiempoFin - tiempoIn, ' Segundos')