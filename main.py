import cv2
from modules.camera import start_camera
from modules.detection import detect_objects, draw_detections
from modules.segmentation import segment_by_color
from modules.filters import apply_filter
from modules.ar_overlay import overlay_image
from modules.interaction import handle_keyboard


def process_frame(frame):
    # Detect objects
    objects = detect_objects(frame)

    # Draw detections
    frame = draw_detections(frame, objects)

    # Apply filter
    global current_filter
    frame = apply_filter(frame, current_filter)

    return frame


if __name__ == '__main__':
    current_filter = 'none'
    start_camera(process_frame)
