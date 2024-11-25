import cv2

# Load pre-trained Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def detect_objects(frame, cascade=face_cascade):
    """
    Detect objects (e.g., faces) in a frame using Haar cascades.
    Args:
        frame (numpy.ndarray): The input frame.
        cascade (CascadeClassifier): Haar cascade to use for detection.
    Returns:
        list: List of bounding boxes [(x, y, w, h)].
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    objects = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
    return objects


def draw_detections(frame, objects):
    """
    Draw rectangles around detected objects.
    Args:
        frame (numpy.ndarray): The input frame.
        objects (list): List of bounding boxes [(x, y, w, h)].
    Returns:
        numpy.ndarray: The frame with detections drawn.
    """
    for (x, y, w, h) in objects:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return frame
