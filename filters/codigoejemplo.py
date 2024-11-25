import math

def calcular_angulo_vision(focal_length, sensor_width):
    return 2 * math.atan(sensor_width / (2 * focal_length)) * (180 / math.pi)

# Parámetros del sensor y longitudes focales
sensor_width = 36  # Ancho del sensor en mm (equivalente a 35mm full-frame)
focal_lengths = [18, 35, 50, 85, 135, 200]  # Longitudes focales en mm

print("Longitud Focal (mm) | Ángulo de Visión (grados)")
print("---------------------|--------------------------")
for focal in focal_lengths:
    angle_of_view = calcular_angulo_vision(focal, sensor_width)
    print(f"{focal:<20} | {angle_of_view:.2f}")