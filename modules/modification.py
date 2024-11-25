import cv2
import numpy as np


def adjust_brightness_saturation(frame, brightness=0, saturation=0):
    """
    Adjust the brightness and saturation of a frame.
    Args:
        frame (numpy.ndarray): The input frame.
        brightness (int): Brightness adjustment value (-100 to 100).
        saturation (int): Saturation adjustment value (-100 to 100).
    Returns:
        numpy.ndarray: Modified frame.
    """
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
    h, s, v = cv2.split(hsv)

    # Adjust saturation and brightness
    s = np.clip(s + saturation, 0, 255)
    v = np.clip(v + brightness, 0, 255)

    hsv_modified = cv2.merge([h, s, v])
    return cv2.cvtColor(hsv_modified.astype(np.uint8), cv2.COLOR_HSV2BGR)
