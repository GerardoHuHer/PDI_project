import cv2
import numpy as np


def perimeter_detection(frame, threshold=100):
    """
    Detect the perimeter of objects in the frame using thresholding.
    Args:
        frame (numpy.ndarray): The input video frame.
        threshold (int): Threshold value for binary segmentation.
    Returns:
        numpy.ndarray: Frame with detected perimeters.
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    perimeter_frame = frame.copy()
    cv2.drawContours(perimeter_frame, contours, -1, (0, 255, 0), 2)

    return perimeter_frame
