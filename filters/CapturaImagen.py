import cv2
import time


def capturar_imagenes(video_source=0, output_folder="/home/gd_15/Escritorio/Procesamiento_Imagenes_UP/fotos", intervalo=1, max_frames=10):

    cap = cv2.VideoCapture(video_source)
    contador = 0

    while contador < max_frames:
        ret, frame = cap.read()
        if not ret:
            break

        # Guardar la imagen capturada
        cv2.imwrite(f"{output_folder}/frame_{contador:04d}.jpg", frame)
        print(f"Imagen capturada: frame_{contador:04d}.jpg")
        contador += 1

        # Esperar un intervalo antes de capturar la siguiente imagen
        time.sleep(intervalo)

    cap.release()
    cv2.destroyAllWindows()


capturar_imagenes()
