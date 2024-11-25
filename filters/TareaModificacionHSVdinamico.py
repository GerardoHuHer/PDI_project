import cv2
import numpy as np

path = "D:\\Procesamiento_Imagenes_UP\\arbol.jpg"
imagen = cv2.imread(path)

imagen_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

tonalidad = 0
saturacion = 0
intensidad = 0

boton_pos = (20, 20) 
boton_size = (150, 50)

altura_extra = 100

def dibujar_boton(area_control, texto):
    cv2.rectangle(area_control, boton_pos, (boton_pos[0] + boton_size[0], boton_pos[1] + boton_size[1]), (0, 255, 0), -1)
    cv2.putText(area_control, texto, (boton_pos[0] + 10, boton_pos[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

def clic_en_boton(x, y):
    y -= imagen.shape[0]
    if 0 <= y <= boton_size[1] and boton_pos[0] <= x <= boton_pos[0] + boton_size[0]:
        return True
    return False

def actualizar_imagen():
    nueva_hsv = imagen_hsv.copy()
    nueva_hsv[:, :, 0] = (nueva_hsv[:, :, 0] + tonalidad) % 180 
    nueva_hsv[:, :, 1] = np.clip(nueva_hsv[:, :, 1] + saturacion, 0, 255) 
    nueva_hsv[:, :, 2] = np.clip(nueva_hsv[:, :, 2] + intensidad, 0, 255) 
    return cv2.cvtColor(nueva_hsv, cv2.COLOR_HSV2BGR)

def callback_clic(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        if y > imagen.shape[0] and clic_en_boton(x, y):
            imagen_guardada = actualizar_imagen()
            cv2.imwrite("modificacionHSV.jpg", imagen_guardada) 
            print("Imagen guardada como 'modificacionHSV.jpg'.")

def cambiar_tonalidad(x):
    global tonalidad
    tonalidad = x

def cambiar_saturacion(x):
    global saturacion
    saturacion = x

def cambiar_intensidad(x):
    global intensidad
    intensidad = x

cv2.namedWindow('Modificación HSV')
cv2.setMouseCallback('Modificación HSV', callback_clic)
cv2.createTrackbar('Tonalidad', 'Modificación HSV', 0, 179, cambiar_tonalidad)
cv2.createTrackbar('Saturación', 'Modificación HSV', 0, 255, cambiar_saturacion)
cv2.createTrackbar('Intensidad', 'Modificación HSV', 0, 255, cambiar_intensidad)

while True:
    imagen_modificada = actualizar_imagen()

    area_extendida = np.zeros((imagen.shape[0] + altura_extra, imagen.shape[1], 3), dtype=np.uint8)
    
    area_extendida[:imagen.shape[0], :, :] = imagen_modificada
    
    dibujar_boton(area_extendida[imagen.shape[0]:, :, :], "Guardar")

    cv2.imshow('Modificación HSV', area_extendida)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
