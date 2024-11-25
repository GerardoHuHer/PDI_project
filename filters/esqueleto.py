import cv2
import numpy as np

path: str = "D:\\Procesamiento_Imagenes_UP\\TareaMascaras\\arbol.jpg"
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

el_estruc = cv2.getStructuringElement(cv2.MORPH_CROSS, (15, 15))
esqueleto = np.zeros(img.shape, np.uint8)
img_temp = img.copy()

while True:
    apertura = cv2.morphologyEx(img_temp, cv2.MORPH_OPEN, el_estruc)
    temp = cv2.subtract(img_temp, apertura)
    eroded = cv2.erode(img_temp, el_estruc)
    esqueleto = cv2.bitwise_or(esqueleto, temp)
    img_temp = eroded.copy()
    if cv2.countNonZero(img_temp) == 0:
        break

cv2.imshow("Esqueleto", esqueleto)
cv2.waitKey(0)
cv2.destroyAllWindows()