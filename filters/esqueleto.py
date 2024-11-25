import cv2
import numpy as np


def skeletonize(frame):
    """
    Skeletonize the objects in the frame.
    Args:
        frame (numpy.ndarray): The input video frame.
    Returns:
        numpy.ndarray: Skeletonized frame.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    skeleton = np.zeros_like(binary)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    while True:
        eroded = cv2.erode(binary, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(binary, temp)
        skeleton = cv2.bitwise_or(skeleton, temp)
        binary = eroded.copy()

        if cv2.countNonZero(binary) == 0:
            break

    return cv2.cvtColor(skeleton, cv2.COLOR_GRAY2BGR)
